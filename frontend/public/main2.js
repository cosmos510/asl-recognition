document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("myForm");
    
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
});