import os
import re
from datetime import datetime
import xml.etree.ElementTree as ET
import toml

def extract_title_and_description(filepath):
    """Extract the title (first # heading) and the description (paragraph after it) from a markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    title = None
    description = None
    for i, line in enumerate(lines):
        if line.startswith('#') and not title:
            title = line.strip('#').strip()
            # Look for the first non-empty line after the title
            for desc_line in lines[i + 1:]:
                desc_line = desc_line.strip()
                if desc_line:
                    description = desc_line
                    break
            break

    return title, description

def parse_date_from_filename(filename):
    """Parse the date from the filename in DD_MM_YY format."""
    match = re.match(r'(\d{2})_(\d{2})_(\d{2})\.md$', filename)
    if match:
        day, month, year = map(int, match.groups())
        year += 2000
        return datetime(year, month, day)
    return None

def get_file_creation_date(filepath):
    """Get the file creation date as a fallback."""
    timestamp = os.path.getctime(filepath)
    return datetime.fromtimestamp(timestamp)

def read_book_config(src_dir):
    """Read the book.toml file for RSS configuration."""
    config_path = os.path.join('.', 'book.toml')
    if not os.path.exists(config_path):
        raise FileNotFoundError("book.toml not found in the src directory.")

    with open(config_path, 'r', encoding='utf-8') as f:
        config = toml.load(f)

    rss_config = config.get('rss', {})
    base_url = rss_config.get('base_url', 'http://example.com')
    title = rss_config.get('title', 'MD Book RSS Feed')
    description = rss_config.get('description', 'An RSS feed of markdown entries.')

    return base_url, title, description

def generate_rss(src_dir):
    """Generate an RSS feed from markdown files in the specified src directory."""
    base_url, feed_title, feed_description = read_book_config(src_dir)

    rss = ET.Element('rss', version="2.0")
    channel = ET.SubElement(rss, 'channel')

    ET.SubElement(channel, 'title').text = feed_title
    ET.SubElement(channel, 'link').text = base_url
    ET.SubElement(channel, 'description').text = feed_description

    for filename in sorted(os.listdir(src_dir)):
        if filename.endswith('.md') and filename != "SUMMARY.md" and filename != "o_que.md":
            filepath = os.path.join(src_dir, filename)

            date = parse_date_from_filename(filename) or get_file_creation_date(filepath)
            title, description = extract_title_and_description(filepath)

            if title and description:
                item = ET.SubElement(channel, 'item')
                ET.SubElement(item, 'title').text = title
                ET.SubElement(item, 'description').text = description
                html_filename = filename.replace('.md', '.html')
                ET.SubElement(item, 'link').text = f"{base_url}/{html_filename}"
                ET.SubElement(item, 'pubDate').text = date.strftime('%a, %d %b %Y %H:%M:%S +0000')

    ET.indent(rss, space="  ", level=0)
    tree = ET.ElementTree(rss)
    output_path = os.path.join(src_dir, 'rss.xml')
    tree.write(output_path, encoding='utf-8', xml_declaration=True)

if __name__ == "__main__":
    src_directory = "./src"  # Adjust this path to your src folder
    generate_rss(src_directory)
    print("RSS feed generated at src/rss.xml")
