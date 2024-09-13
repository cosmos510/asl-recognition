from app.models import User
from .forms import RegisterForm
from django.contrib import messages
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate 
from .forms import LoginForm
from django.contrib.auth import authenticate, login as auth_login

import cv2
import mediapipe as mp
import pickle
import numpy as np

# Load the trained model
model_dict = pickle.load(open('/usr/src/app/model1.p', 'rb'))
model = model_dict['model']

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

global_predicted_character = "No prediction"  # Initialize global variable


def get_prediction(request):
    global global_predicted_character
    return JsonResponse({'prediction': global_predicted_character})


@csrf_exempt
def upload_frame(request):
    global global_predicted_character

    if request.method == 'POST':
        if 'file' not in request.FILES:
            return JsonResponse(
                {'status': 'failed', 'error': 'No file part in the request'}, status=400)

        file = request.FILES['file']
        if file.size == 0:
            return JsonResponse(
                {'status': 'failed', 'error': 'Empty file uploaded'}, status=400)

        # Read the uploaded image
        image = file.read()

        # Convert the image to a numpy array
        np_arr = np.frombuffer(image, np.uint8)

        # Decode the image with OpenCV
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

        # Convert the image to RGB (if your model expects RGB input)
        frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Process the frame for hand landmarks
        results = hands.process(frame_rgb)
        if results.multi_hand_landmarks:
            data_aux = []
            x_ = []
            y_ = []

            hand_landmarks = results.multi_hand_landmarks[0]
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

            if len(data_aux) == 42:
                data_aux_np = np.array(data_aux).reshape(1, -1)
                prediction = model.predict(data_aux_np)
                global_predicted_character = prediction[0]
        else:
            global_predicted_character = "No hand detected"

        return JsonResponse({'prediction': global_predicted_character})

    return JsonResponse(
        {'status': 'failed', 'error': 'Invalid request method'}, status=400)


def video_feed(request):
    def generate():
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

        while True:
            ret, frame = cap.read()
            if not ret:
                continue

            # Process frame as needed
            ret, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    return StreamingHttpResponse(
        generate(),
        content_type='multipart/x-mixed-replace; boundary=frame')


def predict(request):
    return render(request, 'predict.html')


def about(request):
    return render(request, 'about.html')

def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the new user
            login(request, user)  # Log the user in
            messages.success(request, 'Your account has been created and you are now logged in!')
            return JsonResponse({'success': True, 'message': 'Registration successful!'})
        else:
            # Include form errors in the JSON response
            return JsonResponse({'success': False, 'errors': form.errors.as_json()})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Get cleaned data
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Authenticate user
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)  # Log the user in
                messages.success(request, 'You are now logged in!')
                return JsonResponse({
                    'success': True,
                    'message': 'Login successful!',
                    'redirect_url': '/'  # Or any other URL you want to redirect to
                })
            else:
                return JsonResponse({'success': False, 'error': 'Invalid username or password'})
        else:
            # Include form errors in the JSON response
            return JsonResponse({'success': False, 'errors': form.errors.as_json()})
    
    # Handle GET requests or invalid POST requests
    form = LoginForm()
    return render(request, 'login.html', {'form': form})