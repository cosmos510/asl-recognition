import cv2
import pickle
import numpy as np
import mediapipe as mp

from django.contrib import messages
from django.http import JsonResponse, StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth import get_user_model

from .forms import RegisterForm, LoginForm, FeedbackForm

User = get_user_model()
model_dict = pickle.load(open('/usr/src/app/model1.p', 'rb'))
model = model_dict['model']

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

global_predicted_character = "No prediction"


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
        image = file.read()
        np_arr = np.frombuffer(image, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        frame_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
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
            ret, jpeg = cv2.imencode('.jpg', frame)
            frame = jpeg.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

    return StreamingHttpResponse(
        generate(),
        content_type='multipart/x-mixed-replace; boundary=frame')


def predict(request):
    return render(request, 'predict.html')


@login_required
def about(request):
    return render(request, 'about.html')


def home(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.save()
            login(request, user)
            messages.success(
                request, 'Your account has been created and you are now logged in!')
            return JsonResponse(
                {'success': True, 'message': 'Registration successful!'})
        else:
            errors = {}
            for field, field_errors in form.errors.items():
                if field == "__all__":
                    errors["non_field_errors"] = field_errors
                else:
                    errors[field] = field_errors
            return JsonResponse({'success': False, 'errors': errors})
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                response = JsonResponse({
                    'success': True,
                    'message': 'Login successful!',
                    'redirect_url': '/'
                })
                response.set_cookie('user_id', user.user_id, max_age=3600)
                messages.success(request, 'You are now logged in!')
                return response
            else:
                return JsonResponse(
                    {'success': False, 'error': 'Invalid username or password'})
        else:
            return JsonResponse(
                {'success': False, 'errors': form.errors.as_json()})

    form = LoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save(commit=False)
            feedback.user = request.user
            feedback.save()
            return redirect('/')
    else:
        form = FeedbackForm()

    return render(request, 'add_feedback.html', {'form': form})
