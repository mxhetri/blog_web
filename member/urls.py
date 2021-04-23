from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'member'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
]