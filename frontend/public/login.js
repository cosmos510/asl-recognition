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
    const form = document.getElementById("loginForm");

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
                    alert("Login successful!");
                    window.location.href = data.redirect_url || "/";
                } else {
                    alert("Login failed: " + (data.error || "An error occurred."));
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert("An unexpected error occurred. Please try again.");
            });
        });
    }
});