import os

from django.http import HttpResponse
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse

from app.users.forms import UserAdminCreateForm
from app.users.models import User


class UserTestCase(TestCase):

    client = Client()

    def setUp(self):
        self.client = Client()
        self.credentials = {
            "username": "testuser",
            "email": "test@test.com",
            "phone_number": 123123123,
            "role": 1,
            "password": "testpassword",
        }
        self.client.user = User.objects.create_user(**self.credentials)
        self.my_admin = User.objects.create_superuser("admin", "password")

    def test_create_user(self):
        url = reverse("register")

        data = {
            "username": "testuser1",
            "email": "test1@test.com",
            "phone_number": 123123123,
            "role": 1,
            "password1": "testpassword",
            "password2": "testpassword",
        }

        response = self.client.post(url, data=data, format="json", follow=True)

        self.assertEqual(User.objects.count(), 2)
        self.assertEqual(response.status_code, 200)

    def test_create_admin_user(self):
        self.client.login(username="admin", password="password")

        data = {
            "username": "testuser1",
            "email": "test1@test.com",
            "phone_number": 123123123,
            "role": 2,
            "password1": "testpassword",
            "password2": "testpassword",
        }

        url = reverse("create-admin")

    def test_login(self):
        response = self.client.post(reverse("login"), self.credentials, follow=True)
        self.assertTrue(response.context["user"].is_authenticated)
