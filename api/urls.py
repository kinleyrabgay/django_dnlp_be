from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('release_settings/', views.release_settings, name='release_settings'),
]
