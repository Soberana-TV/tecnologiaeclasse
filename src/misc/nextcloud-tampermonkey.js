// ==UserScript==
// @name         Custom Script for Specific Domain and Path
// @namespace    http://tampermonkey.net/
// @version      0.1
// @description  Run specific JavaScript on certain pages
// @author       Your Name
// @match        *://joog.local:8080/index.php/apps/notes/note/*
// @grant        GM_registerMenuCommand
// ==/UserScript==

(function() {
    'use strict';

    // Define the function to execute the JavaScript code
    function executeScript(event) {
        event.preventDefault(); // Prevent default click behavior

        var appNavToggle = document.querySelector(".app-navigation-toggle");
        if (appNavToggle) {
            appNavToggle.click();
        }

        var splitPaneList = document.querySelector(".splitpanes__pane.splitpanes__pane-list");
        if (splitPaneList) {
            splitPaneList.remove();
        }

        var textMenubar = document.querySelector(".text-menubar.text-menubar--ready");
        if (textMenubar) {
            textMenubar.remove();
        }

        if (appNavToggle) {
            appNavToggle.remove();
        }

        // Select the first element with the class 'app-menu'
        var element = document.querySelector('.app-menu');

        // Check if the element exists and change its text content
        if (element) {
            element.textContent = "https://teclas.soberana.tv";
        }

        // Select the parent element with the class 'header-end'
        var parentElement = document.querySelector('div.header-end');
        parentElement.style['padding-right'] = '15em';

        // Check if the parent element exists
        if (parentElement) {
            // Select all child div elements within the parent element
            var childElements = parentElement.querySelectorAll('div');

            // Loop through each child element and remove it
            childElements.forEach(function(child) {
                child.remove();
            });
        }

        var editorElement = document.querySelector('div#editor-container');

        if (editorElement) {
            editorElement.style.left = '0em';
            editorElement.style.top = '2em';
        }

        // Create a new div element
        var newNav = document.createElement('nav');

        // Get the current date
        var now = new Date();
        var day = now.getDate();
        var month = now.toLocaleString('pt-BR', { month: 'long' }); // Month in Portuguese
        var year = now.getFullYear();

        // Format the date string
        var dateString = `${day} de ${month} de ${year}`;

        // Set the text content of the new div
        newNav.textContent = dateString;

        // Insert the new div before all other child div elements
        if (parentElement.firstChild) {
            parentElement.insertBefore(newNav, parentElement.firstChild);
        } else {
            // If there are no child elements, simply append the new div
            parentElement.appendChild(newNav);
        }

        // Select the element with the id 'user-menu'
        var userMenu = document.getElementById('user-menu');

        // Check if the element exists
        if (userMenu) {
            // Set the padding of the element
            userMenu.style.padding = '1em';
        }

        // Create a style element to hold the CSS rules
        var style = document.createElement('style');
        style.innerHTML = `
          .app-content-details {
            scrollbar-width: none !important; /* Firefox and others */
          }

          /* WebKit-based browsers */
          .app-content-details::-webkit-scrollbar {
             display: none; /* Hide scrollbars for Chrome, Safari, and newer Edge */
          }
        `;

        // Append the style element to the document head
        document.head.appendChild(style);
    }

    // Function to add click event listeners to .logo-icon elements
    function addClickListeners() {
        // Select all elements with the class .logo-icon
        var logoIcons = document.querySelectorAll('.logo-icon');

        // Add click event listener to each .logo-icon element
        logoIcons.forEach(function(icon) {
            icon.addEventListener('click', executeScript);
        });
    }

    // Call addClickListeners to attach the event listeners
    addClickListeners();

    // Add a button to the Greasemonkey/Tampermonkey menu
    GM_registerMenuCommand("Apply Styles", executeScript);
})();

