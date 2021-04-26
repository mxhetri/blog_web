from django.urls import path
from django.contrib.auth.views import LoginView
# from django.contrib.auth import views as auth_views
from . import views

app_name = 'member'

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    path('edit_profile/', views.UserEditView.as_view(), name='profile_edit'),

    # change password
    # path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    # path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(),
    #      name='password_change_done'),

    #custom change password
    path('password_change/', views.UserPasswordChangeView.as_view(), name='password_change'),
    path('user_profile/<int:pk>', views.UserProfilePageView.as_view(),
         name='user_profile'),
    path('edit_profile/<int:pk>/', views.EditProfilePageView.as_view(),
         name='edit_profile'),



]