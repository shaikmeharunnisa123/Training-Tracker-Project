// Display a message in the browser console

console.log(
    "Freshers Training Progress Tracker started successfully."
);


// Wait until the web page loads

document.addEventListener(
    "DOMContentLoaded",
    function () {

        console.log(
            "Web page loaded successfully."
        );


        // Find all forms on the current page

        const forms =
            document.querySelectorAll("form");


        // Add a submit event to every form

        forms.forEach(
            function (form) {

                form.addEventListener(
                    "submit",
                    function () {

                        console.log(
                            "Form submitted successfully."
                        );

                    }
                );

            }
        );

    }
);