# ASL Recognition

This project is an AI-powered application that recognizes American Sign Language (ASL) alphabet gestures using computer vision. Built with Django and Docker, it provides a straightforward user interface for real-time ASL alphabet recognition.

![Screenshot 2024-10-26 at 17 49 37](https://github.com/user-attachments/assets/fbcda16b-6cc3-41b2-ad49-538eef77bc9c)

![detect](https://github.com/user-attachments/assets/992883c9-82b8-4d3c-854b-21a4e70409e1)

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Real-time ASL Alphabet Recognition**: Detects and classifies ASL alphabet gestures via webcam.
- **Pre-trained CNN Model with Transfer Learning**: Uses a pre-trained CNN model, fine-tuned for ASL.
- **Interactive UI**: A clean, accessible UI built with HTML/CSS and JavaScript.

## Technologies Used
- **Python**: Backend language.
- **Django**: API and application logic.
- **Docker**: Containerization for easy deployment.
- **TensorFlow**: Used for training and implementing neural networks.
- **OpenCV**: Video capture and preprocessing.

## Installation


To set up this project, clone the repository and use Docker Compose:

```bash
git clone https://github.com/cosmos510/asl-recognition.git
cd asl-recognition
docker compose up --build
```
After setup, access the application at http://localhost

## Training Your Own Model

If you want to train your model using your own dataset, place your images of ASL alphabet gestures in the training_model folder and follow the steps below:

	1.	Prepare the Dataset: Ensure your ASL alphabet dataset is in the specified directory.
	2.	Run Data Preparation:
		•	The code processes images to extract hand landmarks and saves the data in a pickle file.
	3.	Train the Model:
		•	The model is trained on the processed data, and the trained model is saved.

## Usage

1. **Access the Application**: Navigate to `http://localhost`.
2.	Recognition: The model processes gestures, displaying recognized ASL alphabet signs.

## Project Structure

- **backend/**: Django project files with API and model logic.
- **frontend/**: HTML, CSS, and JavaScript for the UI.
- **nginx/**: Configuration for serving static files with Nginx.
- **docker-compose.yml**: Docker configuration.

## Contributing

To contribute:

1. **Fork the repository**.
2. **Create a branch** with your feature.
3. **Submit a pull request** for review.

## License

This project is licensed under the MIT License.