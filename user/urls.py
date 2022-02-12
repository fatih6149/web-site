from django.urls import path
from .views import Register, Profile
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', Register, name='user-registration'),
    path('profile/', Profile, name='profile'),
    path('password/', auth_views.PasswordChangeView.as_view(template_name='user/change_password.html')),
]