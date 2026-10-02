(function () {
    "use strict";

    // Content lives in src/notifications.json (published as notifications.json).
    var CONFIG_FILE = "notifications.json";
    var DISMISSED_KEY = "mdbook-notification-dismissed";
    var CYCLE_KEY = "mdbook-notification-cycle";

    var notification = document.getElementById("site-notification");
    if (!notification) {
        return;
    }

    // Place the notice at the top of the text column, same width as the paragraphs.
    var content = document.getElementById("content");
    if (content) {
        content.insertBefore(notification, content.firstChild);
    }

    function readStorage(key) {
        try {
            return window.localStorage.getItem(key);
        } catch (error) {
            return null;
        }
    }

    function writeStorage(key, value) {
        try {
            window.localStorage.setItem(key, value);
        } catch (error) {
            // Storage can be unavailable in private browsing modes.
        }
    }

    function readDismissed() {
        try {
            var list = JSON.parse(readStorage(DISMISSED_KEY));
            return Array.isArray(list) ? list : [];
        } catch (error) {
            return [];
        }
    }

    function pick(candidates, mode) {
        if (mode === "cycle") {
            var index = parseInt(readStorage(CYCLE_KEY), 10);
            if (isNaN(index) || index < 0) {
                index = 0;
            }
            writeStorage(CYCLE_KEY, String(index + 1));
            return candidates[index % candidates.length];
        }
        return candidates[Math.floor(Math.random() * candidates.length)];
    }

    function render(config, item) {
        var label = notification.querySelector("[data-notification-label]");
        var message = notification.querySelector("[data-notification-message]");
        var link = notification.querySelector("[data-notification-link]");
        var dismiss = notification.querySelector("[data-notification-dismiss]");

        label.textContent = item.label || "";
        label.hidden = !item.label;
        message.textContent = item.message;

        if (item.link && item.link.text && item.link.url) {
            link.textContent = item.link.text;
            link.href = item.link.url;
            link.hidden = false;
        }

        if (config.dismissible !== false && item.id) {
            dismiss.hidden = false;
            dismiss.addEventListener("click", function () {
                notification.hidden = true;
                var dismissed = readDismissed();
                if (dismissed.indexOf(item.id) === -1) {
                    dismissed.push(item.id);
                }
                writeStorage(DISMISSED_KEY, JSON.stringify(dismissed));
            });
        }

        notification.hidden = false;
    }

    var root = typeof path_to_root === "string" ? path_to_root : "";

    fetch(root + CONFIG_FILE, { cache: "no-cache" })
        .then(function (response) {
            return response.ok ? response.json() : null;
        })
        .then(function (config) {
            if (!config || !config.enabled || !Array.isArray(config.notifications)) {
                return;
            }

            var dismissed = config.dismissible === false ? [] : readDismissed();
            var candidates = config.notifications.filter(function (item) {
                return item && item.message && dismissed.indexOf(item.id) === -1;
            });

            if (candidates.length === 0) {
                return;
            }

            render(config, pick(candidates, config.mode));
        })
        .catch(function () {
            // Missing or invalid JSON: keep the notice hidden.
        });
})();
