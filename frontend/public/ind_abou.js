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
});

async function loadComponent(url) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`Failed to load ${url}, status: ${response.status}`);
    }
    return await response.text();
}




function displayResult(result) {
    const predictionDiv = document.querySelector('.prediction');
    if (predictionDiv) {
        predictionDiv.innerHTML = `<h2>${result}</h2>`;
    }
}