from django import forms
from app.users.models import User
from django.contrib.auth.forms import UserCreationForm
from app.core.constants import UserRoleE


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'role', 'phone_number', 'password1', 'password2']