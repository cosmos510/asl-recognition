
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('predict/', views.predict, name='predict'),
    path('video_feed/', views.video_feed, name='video_feed'),
    path('get_prediction/', views.get_prediction, name='get_prediction'),
]