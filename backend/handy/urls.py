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
]
