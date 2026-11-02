#!/usr/bin/env python3
"""Sync a Nextcloud Notes note into this mdBook repository."""

from __future__ import annotations

import argparse
import os
import re
import sys
import tempfile
import unicodedata
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse

try:
    import requests
except ImportError:
    print("Error: the 'requests' package is required.  Install with:  pip install requests", file=sys.stderr)
    sys.exit(2)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
API_NOTE_PATH = "/index.php/apps/notes/api/v1/notes/{id}"
API_ATTACHMENT_PATH = "/index.php/apps/notes/api/v1.4/attachment/{id}"
API_SETTINGS_PATH = "/index.php/apps/notes/api/v1/settings"
WEBDAV_PATH = "/remote.php/dav/files/{user}/{path}"
TIMEOUT_SECONDS = 30
SCRIPT_DIR = Path(__file__).resolve().parent
DEFAULT_SRC_DIR = SCRIPT_DIR / "src"

ATTACHMENT_RE = re.compile(r"\.attachments\.(\d+)/([^\s)\]\"'<>]+)")
YOUTUBE_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")

VIDEO_EXTENSIONS = {".mp4", ".webm", ".mov", ".mkv", ".m4v", ".ogv", ".ogg"}
VIDEO_MIME_TYPES = {
    ".mp4": "video/mp4",
    ".m4v": "video/mp4",
    ".webm": "video/webm",
    ".mov": "video/quicktime",
    ".mkv": "video/x-matroska",
    ".ogv": "video/ogg",
    ".ogg": "video/ogg",
}
CONTENT_TYPE_EXTENSIONS = {
    "image/jpeg": ".jpg",
    "image/png": ".png",
    "image/gif": ".gif",
    "image/webp": ".webp",
    "image/svg+xml": ".svg",
    "image/avif": ".avif",
    "video/mp4": ".mp4",
    "video/webm": ".webm",
    "video/quicktime": ".mov",
    "video/x-matroska": ".mkv",
    "video/ogg": ".ogv",
}

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

def _load_dotenv(path: Path) -> dict[str, str]:
    """Minimal .env reader (KEY=VALUE lines, # comments)."""
    values: dict[str, str] = {}
    if not path.is_file():
        return values
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, _, value = line.partition("=")
        values[key.strip()] = value.strip().strip("\"'")
    return values


def load_config() -> tuple[str, str, str]:
    """Return (url, username, password) from env vars or a local .env file."""
    env_url = os.environ.get("NEXTCLOUD_URL")
    env_user = os.environ.get("NEXTCLOUD_USERNAME")
    env_pass = os.environ.get("NEXTCLOUD_APP_PASSWORD")

    if not all((env_url, env_user, env_pass)):
        for candidate in (Path.cwd() / ".env", SCRIPT_DIR / ".env"):
            dot = _load_dotenv(candidate)
            env_url = env_url or dot.get("NEXTCLOUD_URL")
            env_user = env_user or dot.get("NEXTCLOUD_USERNAME")
            env_pass = env_pass or dot.get("NEXTCLOUD_APP_PASSWORD")
            if all((env_url, env_user, env_pass)):
                break

    missing = []
    if not env_url:
        missing.append("NEXTCLOUD_URL")
    if not env_user:
        missing.append("NEXTCLOUD_USERNAME")
    if not env_pass:
        missing.append("NEXTCLOUD_APP_PASSWORD")

    if missing:
        print(
            f"Error: missing required configuration: {', '.join(missing)}\n"
            "Set them as environment variables or in a .env file in the current "
            "directory or next to the script.",
            file=sys.stderr,
        )
        sys.exit(2)

    return env_url.rstrip("/"), env_user, env_pass


# ---------------------------------------------------------------------------
# Input parsing and slugs
# ---------------------------------------------------------------------------

_NOTE_ID_RE = re.compile(r"^\d+$")
_SLUG_RE = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")


def parse_note_input(arg: str) -> tuple[str, str | None]:
    """Return (note_id, base_url_override) for a note ID or note URL."""
    if _NOTE_ID_RE.match(arg):
        return arg, None

    if "://" not in arg:
        arg = "http://" + arg

    parsed = urlparse(arg)
    base_url = f"{parsed.scheme}://{parsed.netloc}".rstrip("/")

    match = re.search(r"/notes/note/(\d+)(?:[/?#].*)?$", parsed.path)
    if not match:
        raise ValueError(
            f"Could not extract a numeric note ID from URL: {arg}\n"
            "Expected a path like /index.php/apps/notes/note/<id>"
        )
    return match.group(1), base_url


def slugify(text: str) -> str:
    """Turn a note title into a safe, URL-friendly slug."""
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = "".join(ch for ch in normalized if not unicodedata.combining(ch))
    slug = re.sub(r"[^a-zA-Z0-9]+", "_", ascii_text).strip("_").lower()
    slug = re.sub(r"_+", "_", slug)
    return slug[:80].rstrip("_")


def normalize_slug(value: str) -> str:
    slug = value.strip()
    if slug.endswith(".md"):
        slug = slug[:-3]
    if not _SLUG_RE.fullmatch(slug) or ".." in slug:
        raise ValueError(
            f"Invalid slug: {value!r}. Use letters, digits, dots, underscores and hyphens."
        )
    return slug


def extract_h1(content: str) -> str | None:
    for line in content.splitlines():
        if not line.strip():
            continue
        match = re.match(r"#\s+(.+?)\s*$", line)
        return match.group(1) if match else None
    return None


def ensure_title(content: str, title: str) -> str:
    first = next((line for line in content.splitlines() if line.strip()), "")
    if re.match(r"#\s+\S", first):
        return content
    body = content.lstrip("\n")
    return f"# {title}\n\n{body}" if body else f"# {title}\n"


# ---------------------------------------------------------------------------
# API interaction
# ---------------------------------------------------------------------------

def fetch_note(base_url: str, note_id: str, username: str, password: str) -> dict:
    url = base_url + API_NOTE_PATH.format(id=note_id)
    try:
        resp = requests.get(
            url,
            auth=(username, password),
            timeout=TIMEOUT_SECONDS,
            headers={"Accept": "application/json"},
        )
    except requests.exceptions.ConnectionError as exc:
        raise RuntimeError(
            f"Could not connect to {base_url} - {exc}\n"
            "Check NEXTCLOUD_URL and network connectivity."
        ) from None
    except requests.exceptions.Timeout:
        raise RuntimeError(f"Request to {base_url} timed out after {TIMEOUT_SECONDS}s.") from None
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"Unexpected request error: {exc}") from None

    if resp.status_code == 401:
        raise RuntimeError(
            "Authentication failed (HTTP 401).\n"
            "Verify NEXTCLOUD_USERNAME and NEXTCLOUD_APP_PASSWORD.\n"
            "Tip: use a Nextcloud *app password*, not your account password."
        )
    if resp.status_code == 403:
        raise RuntimeError("Access denied (HTTP 403). The app password may lack permission.")
    if resp.status_code == 404:
        raise RuntimeError(f"Note {note_id} not found (HTTP 404). Verify the ID.")
    if resp.status_code >= 400:
        raise RuntimeError(f"Server returned HTTP {resp.status_code} for note {note_id}.")

    try:
        data = resp.json()
    except ValueError:
        raise RuntimeError(
            "The server returned a non-JSON response. "
            "The endpoint may not be the Notes REST API."
        ) from None

    if "ocs" in data and isinstance(data["ocs"], dict) and "data" in data["ocs"]:
        data = data["ocs"]["data"]

    if not isinstance(data, dict) or "content" not in data:
        raise RuntimeError(
            "Unexpected API response structure. "
            f"Expected a note object with 'content', got: "
            f"{sorted(data.keys()) if isinstance(data, dict) else type(data)}"
        )
    if not isinstance(data["content"], str):
        raise RuntimeError("Note 'content' field is not a string.")
    return data


def fetch_settings(base_url: str, username: str, password: str) -> dict:
    url = base_url + API_SETTINGS_PATH
    try:
        resp = requests.get(
            url,
            auth=(username, password),
            timeout=TIMEOUT_SECONDS,
            headers={"Accept": "application/json"},
        )
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"Could not load Notes settings: {exc}") from None

    if resp.status_code >= 400:
        raise RuntimeError(f"Could not load Notes settings (HTTP {resp.status_code}).")
    try:
        data = resp.json()
    except ValueError:
        raise RuntimeError("Notes settings endpoint returned non-JSON data.") from None
    if not isinstance(data, dict):
        raise RuntimeError("Unexpected Notes settings response.")
    return data


def _attachment_error(resp: requests.Response, rel_path: str) -> RuntimeError:
    if resp.status_code == 401:
        return RuntimeError("Authentication failed while downloading an attachment (HTTP 401).")
    if resp.status_code == 403:
        return RuntimeError(f"Access denied downloading {rel_path} (HTTP 403).")
    if resp.status_code == 404:
        return RuntimeError(f"Attachment not found: {rel_path} (HTTP 404).")
    return RuntimeError(f"Server returned HTTP {resp.status_code} for attachment {rel_path}.")


def fetch_attachment_webdav(
    base_url: str,
    note: dict,
    rel_path: str,
    username: str,
    password: str,
) -> requests.Response:
    settings = fetch_settings(base_url, username, password)
    notes_path = str(settings.get("notesPath") or "Notes").strip("/")
    category = str(note.get("category") or "").strip("/")
    parts = [notes_path, category, rel_path]
    dav_rel = "/".join(part for part in parts if part)
    url = base_url + WEBDAV_PATH.format(
        user=quote(username, safe=""),
        path=quote(dav_rel, safe="/"),
    )
    try:
        resp = requests.get(
            url,
            auth=(username, password),
            timeout=TIMEOUT_SECONDS,
            stream=True,
        )
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"Could not download attachment {rel_path}: {exc}") from None

    if resp.status_code >= 400:
        error = _attachment_error(resp, rel_path)
        resp.close()
        raise error
    return resp


def fetch_attachment(
    base_url: str,
    note: dict,
    note_id: str,
    rel_path: str,
    username: str,
    password: str,
) -> requests.Response:
    url = base_url + API_ATTACHMENT_PATH.format(id=note_id)
    try:
        resp = requests.get(
            url,
            auth=(username, password),
            params={"path": rel_path},
            timeout=TIMEOUT_SECONDS,
            stream=True,
        )
    except requests.exceptions.RequestException as exc:
        raise RuntimeError(f"Could not download attachment {rel_path}: {exc}") from None

    if resp.status_code == 400:
        resp.close()
        return fetch_attachment_webdav(base_url, note, rel_path, username, password)
    if resp.status_code >= 400:
        error = _attachment_error(resp, rel_path)
        resp.close()
        raise error
    return resp


# ---------------------------------------------------------------------------
# Content transforms
# ---------------------------------------------------------------------------

def _standalone_url(line: str) -> str | None:
    stripped = line.strip()
    match = re.fullmatch(r"<(https?://[^>\s]+)>", stripped)
    if match:
        return match.group(1)
    match = re.fullmatch(
        r"\[(https?://[^\]]+)\]\((https?://\S+?)(?:\s+\(preview\))?\)",
        stripped,
    )
    if match:
        return match.group(2)
    match = re.fullmatch(r"(https?://\S+)", stripped)
    if match:
        return match.group(1)
    return None


def youtube_video_id(url: str) -> str | None:
    try:
        parsed = urlparse(url)
    except ValueError:
        return None

    host = parsed.netloc.lower()
    if host.startswith("www."):
        host = host[4:]

    path = parsed.path
    video = ""

    if host == "youtu.be":
        video = path.strip("/").split("/")[0]
    elif host in {"youtube.com", "m.youtube.com", "youtube-nocookie.com"}:
        if path.rstrip("/") == "/watch":
            video = parse_qs(parsed.query).get("v", [""])[0]
        elif path.startswith("/shorts/"):
            parts = path.split("/")
            video = parts[2] if len(parts) > 2 else ""
        elif path.startswith("/embed/"):
            parts = path.split("/")
            video = parts[2] if len(parts) > 2 else ""
        elif path.startswith("/live/"):
            parts = path.split("/")
            video = parts[2] if len(parts) > 2 else ""
        elif path.startswith("/v/"):
            parts = path.split("/")
            video = parts[2] if len(parts) > 2 else ""
        elif path in {"", "/"}:
            video = parse_qs(parsed.query).get("v", [""])[0]

    return video if YOUTUBE_ID_RE.fullmatch(video) else None


def convert_youtube_links(content: str) -> tuple[str, int]:
    lines = content.splitlines(keepends=True)
    converted = 0
    in_fence = False

    for index, line in enumerate(lines):
        stripped = line.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or stripped.startswith("{{#embed"):
            continue

        url = _standalone_url(line)
        if not url:
            continue
        video_id = youtube_video_id(url)
        if not video_id:
            continue

        if line.endswith("\r\n"):
            newline = "\r\n"
        elif line.endswith("\n"):
            newline = "\n"
        else:
            newline = ""
        lines[index] = f"{{{{#embed https://youtube.com/watch?v={video_id}}}}}{newline}"
        converted += 1

    return "".join(lines), converted


def find_attachment_refs(content: str) -> list[str]:
    refs: list[str] = []
    seen: set[str] = set()
    for match in ATTACHMENT_RE.finditer(content):
        ref = match.group(0)
        if ref not in seen:
            seen.add(ref)
            refs.append(ref)
    return refs


def _extension_from_name(name: str) -> str:
    extension = Path(name).suffix.lower()
    return extension if re.fullmatch(r"\.[a-z0-9]{1,8}", extension) else ""


def choose_extension(filename: str, content_type: str) -> str:
    extension = _extension_from_name(filename)
    if extension:
        return extension
    base_type = content_type.split(";")[0].strip().lower()
    return CONTENT_TYPE_EXTENSIONS.get(base_type, ".bin")


def mime_type_for_extension(extension: str, content_type: str) -> str:
    base_type = content_type.split(";")[0].strip().lower()
    if base_type.startswith(("video/", "image/")):
        return base_type
    return VIDEO_MIME_TYPES.get(extension, "application/octet-stream")


def replace_video_images(content: str, ref: str, src: str, mime: str) -> str:
    pattern = re.compile(
        r"!\[[^\]]*\]\(\s*<?"
        + re.escape(ref)
        + r">?(?:\s+[\"'][^\"']*[\"'])?\s*\)"
    )
    block = f'<video controls>\n  <source src="{src}" type="{mime}">\n</video>'
    return pattern.sub(block, content)


def rewrite_attachment_paths(
    content: str,
    mapping: dict[str, dict[str, object]],
    asset_rel: str,
) -> str:
    if not mapping:
        return content

    refs = sorted(mapping, key=len, reverse=True)
    pattern = re.compile(r"(?:\./)?(?:" + "|".join(re.escape(ref) for ref in refs) + ")")

    for ref, info in mapping.items():
        if not info["is_video"]:
            continue
        src = f"./{asset_rel}/{info['local']}"
        content = replace_video_images(content, ref, src, str(info["mime"]))

    def replace(match: re.Match[str]) -> str:
        ref = match.group(0)
        if ref.startswith("./"):
            ref = ref[2:]
        info = mapping[ref]
        return f"./{asset_rel}/{info['local']}"

    return pattern.sub(replace, content)


def build_summary_entry(title: str, link_name: str) -> str:
    safe_title = title.replace("\\", "\\\\").replace("[", "\\[").replace("]", "\\]")
    safe_title = " ".join(safe_title.split())
    return f"- [{safe_title}]({link_name})"


def update_summary(text: str, title: str, link_name: str) -> tuple[str, bool]:
    entry = build_summary_entry(title, link_name)
    lines = text.splitlines()
    link_pattern = re.compile(r"\]\((?:\./)?" + re.escape(link_name) + r"\)")

    for index, line in enumerate(lines):
        if link_pattern.search(line):
            if line == entry:
                return text, False
            lines[index] = entry
            return "\n".join(lines) + "\n", True

    insert_at = None
    for index, line in enumerate(lines):
        if "o_que.md" in line:
            insert_at = index + 1
            break
    if insert_at is None:
        for index, line in enumerate(lines):
            if line.lstrip().startswith("- ["):
                insert_at = index + 1
                break

    if insert_at is None:
        if lines and lines[-1] != "":
            lines.append("")
        lines.append(entry)
    else:
        lines.insert(insert_at, entry)
    return "\n".join(lines) + "\n", True


# ---------------------------------------------------------------------------
# File output
# ---------------------------------------------------------------------------

def write_text_file(path: Path, content: str) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
    except PermissionError as exc:
        raise RuntimeError(f"Permission denied writing to {path}: {exc}") from None
    except OSError as exc:
        raise RuntimeError(f"Could not write to {path}: {exc}") from None


def download_attachment(
    base_url: str,
    note: dict,
    note_id: str,
    ref: str,
    username: str,
    password: str,
    target_dir: Path,
    index: int,
) -> dict[str, object]:
    filename = unquote(ref.split("/", 1)[1])
    rel_path = unquote(ref)
    resp = fetch_attachment(base_url, note, note_id, rel_path, username, password)
    try:
        content_type = resp.headers.get("Content-Type", "")
        extension = choose_extension(filename, content_type)
        local = f"{index}{extension}"
        target = target_dir / local
        try:
            with target.open("wb") as handle:
                for chunk in resp.iter_content(chunk_size=65536):
                    if chunk:
                        handle.write(chunk)
        except requests.exceptions.RequestException as exc:
            raise RuntimeError(f"Download interrupted for {ref}: {exc}") from None
    finally:
        resp.close()

    return {
        "local": local,
        "is_video": extension in VIDEO_EXTENSIONS
        or content_type.split(";")[0].strip().lower().startswith("video/"),
        "mime": mime_type_for_extension(extension, content_type),
        "content_type": content_type,
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="sync-note.py",
        description=(
            "Fetch a Nextcloud Notes note, write it into src/, update SUMMARY.md, "
            "convert YouTube links to embeds and download attachments."
        ),
    )
    parser.add_argument(
        "note",
        help="Numeric note ID, or a note URL like http://host/index.php/apps/notes/note/23442",
    )
    parser.add_argument(
        "--slug",
        default=None,
        help="Target file name without .md (default: derived from the note title)",
    )
    parser.add_argument(
        "--title",
        default=None,
        help=(
            "Override the title used in SUMMARY.md (and the H1 when the note "
            "content has none)"
        ),
    )
    parser.add_argument(
        "--src-dir",
        default=str(DEFAULT_SRC_DIR),
        help="mdBook source directory (default: <script-dir>/src)",
    )
    parser.add_argument(
        "--summary",
        default=None,
        help="SUMMARY.md path (default: <src-dir>/SUMMARY.md)",
    )
    parser.add_argument(
        "-o", "--output",
        default=None,
        help="Markdown destination (default: <src-dir>/<slug>.md)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files or downloading attachments",
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Print progress details",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        note_id, url_override = parse_note_input(args.note)
    except ValueError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2

    base_url, username, password = load_config()
    if url_override:
        base_url = url_override

    src_dir = Path(args.src_dir).expanduser().resolve()
    if not src_dir.is_dir():
        print(f"Error: source directory not found: {src_dir}", file=sys.stderr)
        return 2

    summary_path = (
        Path(args.summary).expanduser().resolve()
        if args.summary
        else src_dir / "SUMMARY.md"
    )
    if not summary_path.is_file():
        print(f"Error: SUMMARY.md not found: {summary_path}", file=sys.stderr)
        return 2

    if args.verbose:
        print(f"Fetching note {note_id} from {base_url}")

    try:
        note = fetch_note(base_url, note_id, username, password)
        content = note["content"]
        api_title = str(note.get("title") or "").strip()
        title = (args.title or api_title or extract_h1(content) or "").strip()
        title = " ".join(title.splitlines())
        if not title:
            raise RuntimeError("The note has no title. Pass one with --title.")

        if args.slug:
            try:
                slug = normalize_slug(args.slug)
            except ValueError as exc:
                print(f"Error: {exc}", file=sys.stderr)
                return 2
        else:
            slug = slugify(title) or f"note_{note_id}"

        dest_path = (
            Path(args.output).expanduser().resolve()
            if args.output
            else src_dir / f"{slug}.md"
        )
        if dest_path.is_dir():
            raise RuntimeError(f"Output path is a directory: {dest_path}")

        asset_dir = dest_path.parent / slug
        try:
            asset_rel = asset_dir.relative_to(src_dir).as_posix()
            link_name = dest_path.relative_to(src_dir).as_posix()
        except ValueError:
            asset_rel = slug
            link_name = f"{slug}.md"
            print(
                f"Warning: {dest_path} is outside {src_dir}; SUMMARY.md may link incorrectly.",
                file=sys.stderr,
            )

        if args.verbose:
            print(f"Title: {title}")
            print(f"Slug: {slug}")
            print(f"Destination: {dest_path}")

        refs = find_attachment_refs(content)
        mapping: dict[str, dict[str, object]] = {}
        temp_dir = None

        if refs and not args.dry_run:
            temp_dir = tempfile.TemporaryDirectory(prefix=".sync-note-", dir=str(src_dir))

        try:
            for index, ref in enumerate(refs, start=1):
                filename = unquote(ref.split("/", 1)[1])
                if args.dry_run:
                    extension = choose_extension(filename, "")
                    mapping[ref] = {
                        "local": f"{index}{extension}",
                        "is_video": extension in VIDEO_EXTENSIONS,
                        "mime": mime_type_for_extension(extension, ""),
                    }
                    continue

                info = download_attachment(
                    base_url,
                    note,
                    note_id,
                    ref,
                    username,
                    password,
                    Path(temp_dir.name),
                    index,
                )
                mapping[ref] = info
                if args.verbose:
                    print(f"Downloaded attachment: {ref} -> {asset_dir / str(info['local'])}")

            new_content = rewrite_attachment_paths(content, mapping, asset_rel)
            new_content, converted = convert_youtube_links(new_content)
            new_content = ensure_title(new_content, title).rstrip("\n") + "\n"

            try:
                summary_text = summary_path.read_text(encoding="utf-8")
            except OSError as exc:
                raise RuntimeError(f"Could not read {summary_path}: {exc}") from None
            new_summary, summary_changed = update_summary(summary_text, title, link_name)

            if args.dry_run:
                print(f"[dry-run] Note {note_id}: {title}")
                print(f"[dry-run] Would write {dest_path}")
                if mapping:
                    print(f"[dry-run] Would download {len(mapping)} attachment(s) to {asset_dir}/")
                if converted:
                    print(f"[dry-run] Would convert {converted} YouTube link(s) to embeds")
                if summary_changed:
                    print(f"[dry-run] Would update {summary_path}")
                else:
                    print(f"[dry-run] {summary_path} is already up to date")
                return 0

            if mapping:
                asset_dir.mkdir(parents=True, exist_ok=True)
                for info in mapping.values():
                    os.replace(
                        Path(temp_dir.name) / str(info["local"]),
                        asset_dir / str(info["local"]),
                    )

            write_text_file(dest_path, new_content)
            if summary_changed:
                write_text_file(summary_path, new_summary)

            print(f"Wrote {dest_path}")
            if mapping:
                print(f"Downloaded {len(mapping)} attachment(s) to {asset_dir}/")
            if converted:
                print(f"Converted {converted} YouTube link(s) to embeds")
            if summary_changed:
                print(f"Updated {summary_path}")
            else:
                print(f"{summary_path} is already up to date")
            return 0
        finally:
            if temp_dir is not None:
                temp_dir.cleanup()

    except RuntimeError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1
    except OSError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
