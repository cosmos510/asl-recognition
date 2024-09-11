document.addEventListener("DOMContentLoaded", function() {
    
    fetch('/header.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('header-container').innerHTML = data;
        })
        .catch(error => console.error('Error loading header:', error));
        fetch('/footer.html')
        .then(response => response.text())
        .then(data => {
            document.getElementById('footer-container').innerHTML = data;
        })
        .catch(error => console.error('Error loading footer:', error));

    // Handle form submission
    const form = document.getElementById("myForm");
    
    if (form) { 
        form.addEventListener("submit", function(event) {
            event.preventDefault(); 

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