function getCookie(name) {

    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {

        const cookies = document.cookie.split(";");

        for (let cookie of cookies) {

            cookie = cookie.trim();

            if (cookie.startsWith(name + "=")) {

                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));

                break;

            }
        }
    }

    return cookieValue;
}

const csrftoken = getCookie("csrftoken");













console.log("Training Tracker Loaded");

document.addEventListener("DOMContentLoaded", function () {

    console.log("DOM Loaded");

    // ==========REGISTER FORM ============

    const registerForm = document.getElementById("registerForm");

    console.log(registerForm);

    if (registerForm) {

        console.log("Register form found");

        registerForm.addEventListener("submit", async function (e) {

            e.preventDefault();

    console.log("Register button clicked");

    const formData = {
        employee_id: document.getElementById("id_employee_id").value,
        name: document.getElementById("id_name").value,
        email: document.getElementById("id_email").value,
        phone: document.getElementById("id_phone").value,
        technology: document.getElementById("id_technology").value,
        batch: document.getElementById("id_batch").value,
        joining_date: document.getElementById("id_joining_date").value
    };

    console.log(formData);

    const response = await fetch("/api/mongo/freshers/", {
    method: "POST",
    headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrftoken
    },
    body: JSON.stringify(formData)
});

const result = await response.json();

console.log(result);

alert(result.message);

        });

    } else {

        console.log("Register form NOT found");

    }


    //======== DASHBOARD PAGE ========

    const fresherCard = document.getElementById("freshersCard");
    if (freshersCard) {

        freshersCard.addEventListener("click", async function () {

            console.log("Freshers card clicked");

            const response = await fetch("/api/mongo/freshers/");

            const freshers = await response.json();

            console.log(freshers);
            const container = document.getElementById("freshersContainer");
            let table = `
                        <h2>Fresher Details</h2>

                        <table border="1">

                        <tr>
                            <th>Employee ID</th>
                            <th>Name</th>
                            <th>Email</th>
                            <th>Technology</th>
                            <th>Batch</th>
                        </tr>`;
            
                freshers.forEach(function(fresher){

                                table += `
                                <tr>
                                    <td>${fresher.employee_id}</td>
                                    <td>${fresher.name}</td>
                                    <td>${fresher.email}</td>
                                    <td>${fresher.technology}</td>
                                    <td>${fresher.batch}</td>
                                </tr>
                                `;

                                });

                table += "</table>";
                container.innerHTML = table;

        });



    }

});