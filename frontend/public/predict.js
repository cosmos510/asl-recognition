async function setupWebcam() {
    const webcamElement = document.getElementById('webcam');
    try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        webcamElement.srcObject = stream;
    } catch (err) {
        console.error('Error accessing webcam: ', err);
    }
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function sendFrameToServer(blob) {
    if (!(blob instanceof Blob)) {
        console.error('Expected a Blob, but got:', blob);
        return;
    }

    const formData = new FormData();
    formData.append('file', blob, 'frame.jpg');

    fetch("/upload_frame/", {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': getCookie('csrftoken')
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('prediction-text').innerText = data.prediction || 'No prediction';
    })
    .catch(error => console.error('Error:', error));
}

function captureFrame() {
    const videoElement = document.getElementById('webcam');
    const canvas = document.createElement('canvas');
    canvas.width = videoElement.videoWidth;
    canvas.height = videoElement.videoHeight;
    
    const context = canvas.getContext('2d');
    context.drawImage(videoElement, 0, 0, canvas.width, canvas.height);
    
    if (canvas.toBlob) {
        canvas.toBlob(blob => {
            if (blob) {
                sendFrameToServer(blob);
            } else {
                console.error('Failed to create blob from canvas.');
            }
        }, 'image/jpeg');
    } else {
        console.error('Canvas API does not support toBlob.');
    }
}

function addLetterToWord() {
    const predictedLetter = document.getElementById('prediction-text').innerText;
    const currentWordElement = document.getElementById('current-word');
    if (predictedLetter.trim() === 'space') {
        currentWordElement.innerText += ' '; 
    } else if (predictedLetter && predictedLetter !== 'No hand detected') {
        currentWordElement.innerText += predictedLetter;
    } else {
        alert("No valid hand detected. Please ensure your hand is visible to the camera.");
    }
}
function clearWord() {
    document.getElementById('current-word').innerText = '';
}

document.addEventListener("DOMContentLoaded", function() {
    document.getElementById('confirm-letter').addEventListener('click', addLetterToWord);
    document.getElementById('clear-word').addEventListener('click', clearWord);
    
    setupWebcam();
    setInterval(captureFrame, 1000);
});