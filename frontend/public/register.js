document.addEventListener("DOMContentLoaded", function() {

    

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
                    alert("Registration Successful, you are now log in!");
                    window.location.href = "/";
                } else {
                    displayErrors(data.errors);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        });
    }

    function displayErrors(errors) {
        document.querySelectorAll('.error-message').forEach(container => container.textContent = '');

        for (const [field, messages] of Object.entries(errors)) {
            const errorContainer = document.getElementById(`${field}-error`);
            if (errorContainer) {
                errorContainer.textContent = Array.isArray(messages) ? messages.join(', ') : messages;
            }
        }
    }
});