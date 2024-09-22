
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