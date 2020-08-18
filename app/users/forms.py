from django import forms
from app.users.models import User
from django.contrib.auth.forms import UserCreationForm
from app.users.constants import UserRoleE


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']


class UserAdminCreateForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ['username', 'email', 'phone_number', 'role', 'password1', 'password2']

