# ASL Recognition

This project is an AI-powered application that recognizes American Sign Language (ASL) gestures using computer vision. Built with Django and Docker, it provides a straightforward user interface for real-time ASL recognition.

![Screenshot 2024-10-26 at 17 49 37](https://github.com/user-attachments/assets/fbcda16b-6cc3-41b2-ad49-538eef77bc9c)


## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Model Training](#model-training)
- [Contributing](#contributing)
- [License](#license)

## Features
- **Real-time ASL Gesture Recognition**: Detects and classifies ASL gestures via webcam.
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

## Usage

1. **Access the Application**: Navigate to `http://localhost`.
2. **Recognition**: The model processes gestures, displaying recognized ASL signs.

## Project Structure

- **backend/**: Django project files with API and model logic.
- **frontend/**: HTML, CSS, and JavaScript for the UI.
- **nginx/**: Configuration for serving static files with Nginx.
- **docker-compose.yml**: Docker configuration.

## Model Training

The ASL recognition model is based on a CNN, trained with ASL datasets. Fine-tuning allows for accurate gesture recognition. Scripts for further customization are included.

## Contributing

To contribute:

1. **Fork the repository**.
2. **Create a branch** with your feature.
3. **Submit a pull request** for review.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
