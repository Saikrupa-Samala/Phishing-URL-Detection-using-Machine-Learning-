document.addEventListener("DOMContentLoaded", function () {

    const form = document.querySelector("form");
    const urlInput = document.getElementById("url");
    const button = document.querySelector("button");


    // Form validation
    if (form) {

        form.addEventListener("submit", function (event) {

            const url = urlInput.value.trim();

            if (url === "") {

                event.preventDefault();

                alert("Please enter a URL.");

                return;
            }


            // Basic URL validation
            try {

                new URL(url);

            } catch (error) {

                event.preventDefault();

                alert(
                    "Please enter a valid URL.\n\nExample: https://example.com"
                );

                return;
            }


            // Change button while Flask processes the request
            button.disabled = true;

            button.textContent = "Analyzing...";

        });

    }


    // Automatically focus on URL input
    if (urlInput) {

        urlInput.focus();

    }

});