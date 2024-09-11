// main.js

document.addEventListener("DOMContentLoaded", function() {
    
    // Load header
    fetch('/header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header-container').innerHTML = data;
        })
        .catch(error => console.error('Error loading header:', error));

    // Handle form submission
    const form = document.getElementById("myForm");
    
    if (form) { // Check if the form exists on the page
        form.addEventListener("submit", function(event) {
            event.preventDefault(); // Prevent default form submission

            const formData = new FormData(form);

            fetch(form.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-Requested-With': 'XMLHttpRequest',
                    'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert("Registration Successful!");
                    window.location.href = "/"; // Redirect to the homepage or any other page
                } else {
                    alert("Registration failed. Please correct the errors.");
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }
});