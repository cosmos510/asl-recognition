from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('predict/', views.predict, name='predict'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('get_prediction/', views.get_prediction, name='get_prediction'),
    path('upload_frame/', views.upload_frame, name='upload_frame'),
    path('about/', views.about, name='about'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('feedback/', views.add_feedback, name='add_feedback'),
    path('minigame/', views.minigame, name='minigame'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('api/user-status/', views.get_user_status, name='user_status'),
]
