from django.contrib.auth.models import AbstractUser
from django.db import models

from phone_field import PhoneField

from app.core.constants import UserRoleE


class User(AbstractUser):
    phone_number = PhoneField()
    role = models.IntegerField(choices=UserRoleE.choices(), default=1)
