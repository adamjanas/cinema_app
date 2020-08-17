from django.db import models
from django.contrib.auth.models import AbstractUser
from phone_field import PhoneField
from app.core.constants import UserRoleE


class User(AbstractUser):
    phone_number = PhoneField()
    role = models.IntegerField(choices=UserRoleE.choices(), null=True, blank=True, default=1)
