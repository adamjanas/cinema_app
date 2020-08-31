import os

from app.users.forms import UserAdminCreateForm
from app.users.models import User
from django.test import TestCase
from django.test.client import Client


class FormTestCase(TestCase):

    client = Client()

    def setUp(self):

        self.client = Client()
        self.my_admin = User.objects.create_superuser("admin", "password")

    def test_admin_create_form_with_no_phone_number(self):
        self.client.login(username="admin", password="password")

        data = {
            "username": "testuser",
            "email": "test@test.com",
            "phone_number": None,
            "role": 1,
            "password1": "testpassword",
            "password2": "testpassword",
        }

        form = UserAdminCreateForm(data=data)

        self.assertFalse(form.is_valid())

    def test_admin_create_form_with_no_role(self):
        self.client.login(username="admin", password="password")

        data = {
            "username": "testuser",
            "email": "test@test.com",
            "phone_number": 123123123,
            "role": None,
            "password1": "testpassword",
            "password2": "testpassword",
        }

        form = UserAdminCreateForm(data=data)

        self.assertFalse(form.is_valid())
