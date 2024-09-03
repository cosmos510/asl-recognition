import cv2
import mediapipe as mp
import pickle
import numpy as np

class VideoStream:
    model = None
    global_predicted_character = None

    def __init__(self):
        # Load the trained model
        if VideoStream.model is None:
            with open('/Users/maximemartin/test_django/model1.p', 'rb') as f:
                model_dict = pickle.load(f)
                VideoStream.model = model_dict['model']
        
        # Initialize MediaPipe Hands module
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles
        self.hands = self.mp_hands.Hands(static_image_mode=False, min_detection_confidence=0.3)
        
    def generate(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            data_aux = []
            x_ = []
            y_ = []

            H, W, _ = frame.shape
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Process the frame for hand landmarks
            results = self.hands.process(frame_rgb)
            if results.multi_hand_landmarks:
                # Process only the first detected hand
                hand_landmarks = results.multi_hand_landmarks[0]  # Select only the first hand

                self.mp_drawing.draw_landmarks(
                    frame,  # image to draw
                    hand_landmarks,  # model output
                    self.mp_hands.HAND_CONNECTIONS,  # hand connections
                    self.mp_drawing_styles.get_default_hand_landmarks_style(),
                    self.mp_drawing_styles.get_default_hand_connections_style()
                )

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    x_.append(x)
                    y_.append(y)

                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    data_aux.append(x - min(x_))
                    data_aux.append(y - min(y_))

                # Ensure input is in the correct format for prediction
                if len(data_aux) == 42:  # Ensure feature length matches model expectation
                    data_aux_np = np.array(data_aux).reshape(1, -1)
                    prediction = VideoStream.model.predict(data_aux_np)

                    # Update the global prediction
                    VideoStream.global_predicted_character = prediction[0]

            ret, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    @staticmethod
    def get_latest_prediction():
        return VideoStream.global_predicted_character