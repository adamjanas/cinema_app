from app.core.constants import UserRoleE
from app.users.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "password1", "password2"]


class UserAdminCreateForm(UserCreationForm):
    email = forms.EmailField

    class Meta:
        model = User
        fields = ["username", "email", "phone_number", "role", "password1", "password2"]
