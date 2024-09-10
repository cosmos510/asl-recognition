document.getElementById("myForm").addEventListener("submit", function(event) {
    const submitButton = document.getElementById("submitButton");
    submitButton.disabled = true;
    submitButton.textContent = "Registering...";
});