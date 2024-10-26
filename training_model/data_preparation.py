import os
import pickle
import mediapipe as mp
import cv2
import random
import matplotlib.pyplot as plt

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Adjusting confidence to a lower threshold
hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.1)

# Directory containing the ASL dataset
DATA_DIR = '/Users/maximemartin/detect/ASL_Alphabet_Dataset/asl_alphabet_train'

data = []
labels = []

# Flags for debugging and visualization
DEBUG_MODE = False  # Set to True if you want to see random images without landmarks
DISPLAY_SAMPLE_IMAGES = 5  # Number of images to display for debugging purposes

# Counters for summary
total_images = 0
skipped_images = 0
detected_landmarks = 0

# Option to handle multiple hands
HANDLE_MULTIPLE_HANDS = True  # Set to True to handle multiple hands by selecting the first detected hand

# Iterate through each sub-directory in the dataset directory
for dir_ in os.listdir(DATA_DIR):
    # Iterate through each image in the sub-directory
    for img_path in os.listdir(os.path.join(DATA_DIR, dir_)):
        total_images += 1
        data_aux = []

        x_ = []
        y_ = []

        # Read the image and convert to RGB
        img = cv2.imread(os.path.join(DATA_DIR, dir_, img_path))
        if img is None:
            print(f"Failed to read image {img_path}. Skipping.")
            skipped_images += 1
            continue
        
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process the image to detect hand landmarks
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            # Check if there are multiple hands detected
            if HANDLE_MULTIPLE_HANDS and len(results.multi_hand_landmarks) > 1:
                # Option: Choose the first hand detected and ignore the rest
                hand_landmarks = results.multi_hand_landmarks[0]
            else:
                # Continue processing if only one hand detected or all hands are needed
                hand_landmarks = results.multi_hand_landmarks[0]

            # Extract the x and y coordinates of the landmarks
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y

                x_.append(x)
                y_.append(y)

            # Normalize coordinates relative to the minimum x and y values
            for i in range(len(hand_landmarks.landmark)):
                x = hand_landmarks.landmark[i].x
                y = hand_landmarks.landmark[i].y
                data_aux.append(x - min(x_))
                data_aux.append(y - min(y_))

            # Ensure all data samples have the same length
            if len(data) > 0 and len(data_aux) != len(data[0]):
                print(f"Inconsistent data length at image {img_path} in directory {dir_}: expected {len(data[0])}, got {len(data_aux)}")
                continue
            else:
                data.append(data_aux)
                labels.append(dir_)
                detected_landmarks += 1
        else:
            skipped_images += 1
            if DEBUG_MODE and random.random() < (DISPLAY_SAMPLE_IMAGES / total_images):
                print(f"No hand landmarks detected in image {img_path} from directory {dir_}. Skipping this image.")

                # Display the image with no landmarks
                plt.figure(figsize=[10, 10])
                plt.imshow(img_rgb)
                plt.title(f'No Hand Landmarks for {img_path} in {dir_}')
                plt.axis('off')
                plt.show()

# Release MediaPipe resources
hands.close()

# Save the data to a pickle file
with open('data_corrected2.pickle', 'wb') as f:
    pickle.dump({'data': data, 'labels': labels}, f)

# Print summary
print(f"Data preparation complete. {len(data)} samples saved to 'data_corrected.pickle'.")
print(f"Total images processed: {total_images}")
print(f"Images with detected landmarks: {detected_landmarks}")
print(f"Images skipped (no landmarks detected or failed read): {skipped_images}")