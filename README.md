

# ASL Alphabet Recognition

This project is an AI-powered application built to recognize American Sign Language (ASL) alphabet gestures in real-time. Developed with a combination of Django, OpenCV, and Docker, it’s designed to be both accessible and efficient. The app captures hand gestures through a webcam, processes them using a pre-trained CNN model, and displays recognized letters on-screen.

## 🎬 Project Demo
Check out the demo video of the ASL Recognition app in action:

[ASL Recognition Demo](https://github.com/user-attachments/assets/67c19f27-a10f-4b3b-b239-cd83fd91267a)




## 🌐 Project Links

- **Deployed Site**: [Link to Deployed Site](https://cosmos510.github.io/landing_page_asl.io/)
- **GitHub Repository**: [ASL Recognition GitHub Repo](https://github.com/cosmos510/asl-recognition)
- **Project Blog Article**: [Final Project Blog Article](https://www.linkedin.com/feed/update/urn:li:activity:7259995138817409025/)
- **LinkedIn**: [Maxime Martin LinkedIn](https://www.linkedin.com/in/maxime-martin-090731aa/)

---

## 📖 Introduction

My goal was to create an intuitive ASL alphabet recognition tool that could make American Sign Language more accessible to everyone. Although I started this project to push my machine learning skills, it soon became a meaningful way to contribute to accessible tech. This app interprets ASL alphabet gestures with decent real-time accuracy and responsiveness. While it's not perfect, I see this as a stepping stone toward a fully robust ASL recognition solution.

---

## 🧩 Features

* **Real-Time ASL Alphabet Recognition**: Accurately detects ASL alphabet gestures through webcam input.
* **Robust Random Forest Model**: Employs a Random Forest classifier, trained on a comprehensive dataset, to ensure accurate recognition.
* **Simple UI**: Clean, accessible front-end for seamless user experience.

- ![register](https://github.com/user-attachments/assets/5f942d0d-9b11-4ba5-8605-f38944a9b675)


## 🛠️ Technologies Used

- **Python**: For backend logic.
- **Django**: Manages API and app logic.
- **Docker**: Ensures consistent deployment.
- **Scikit-learn**: Powers the deep learning model.
- **OpenCV**: Handles video capture and image processing.

---

## 🧠 Technical Details

1. **Model Choice and Design:**

- **Random Forest Classifier:** A Random Forest classifier is employed to classify the extracted features into corresponding ASL letters. This ensemble learning method is robust to noise and overfitting, making it suitable for image classification tasks.
- **Feature Extraction:** Key features, such as hand shape, orientation, and position, are extracted from each frame using image processing techniques.
- **Model Training:** The model is trained on a dataset of LSF alphabet images, where each image is associated with a corresponding letter. The training process involves fitting the Random Forest classifier to the extracted features and their respective labels.

---

**Note on Model and Training Code:**

To protect the integrity of this project and its future development, details about the specific model and training code have not been included in this repository. If you're interested in testing the full functionality of the app or exploring potential collaborations, please contact me at [your email address].

---

### 2. Data Pipeline and Preprocessing

- **Data Capture**: OpenCV captures frames from the webcam, which are then fed into the model for analysis.
- **Hand Landmark Extraction**: Each frame is processed to isolate hand landmarks, and I implemented a normalization step to ensure x and y coordinates are consistent. This preprocessing step significantly improved the model's accuracy by making gesture inputs more uniform.
- **Real-Time Processing Optimization**: To achieve low-latency, real-time performance, I optimized data flow from capture to prediction to minimize computational load.

- ![data-flow](https://github.com/user-attachments/assets/4b87e55d-e40c-4184-b8a3-01050d87473a)


### 3. Deployment

- **Docker for Portability**: Docker packages dependencies and configurations, ensuring the app runs smoothly on any machine.
- **Web Interface**: A lightweight frontend built with HTML/CSS/JavaScript keeps the app accessible and easy to navigate.

---

## 📂 Project Structure

- **`backend/`**: Contains Django project files for API and model logic.
- **`frontend/`**: Holds HTML, CSS, and JavaScript files for the UI.
- **`nginx/`**: Configuration files to manage static files and improve server performance.
- **`docker-compose.yml`**: Docker setup to manage project containers.

---

## 🤝 Contributing

Contributions are welcome! If you’d like to improve the model, UI, or any other part of the project, here’s how to get involved:

1. **Fork the repository**.
2. **Create a branch** for your feature or fix.
3. **Submit a pull request** for review.

---


## 📓 Project Reflection

Creating this ASL recognition tool was both challenging and rewarding. Initially, it seemed straightforward, but real-time recognition required optimizing the model to reduce frame lag and improve accuracy. Normalizing hand landmarks was a critical breakthrough, allowing the model to handle different hand sizes and gestures consistently. Although the app performs well now, I’d like to keep improving it, especially the UI and extending its recognition capabilities beyond the alphabet.

### What I Learned
Real-time machine learning doesn’t always require powerful hardware; it’s about carefully optimizing each part of the algorithm. Working on this has deepened my interest in AI and accessibility tech.

### Future Goals
My next steps include refining the UI, optimizing the model further, and potentially expanding recognition to full ASL words and phrases.

---

Let’s connect if you’re interested in accessible tech or just want to chat about machine learning!

## 📜 License

This project is licensed under the MIT License, encouraging open collaboration and sharing.
