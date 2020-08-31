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

    def test_user_access_to_create_admin_account_is_forbidden(self):

        self.client.login(username="testuser", password="testpassword")

        url = reverse("create-admin")

        data = {
            "username": "testuser1",
            "email": "test1@test.com",
            "phone_number": 123123123,
            "role": 1,
            "password1": "testpassword",
            "password2": "testpassword",
        }

        response = self.client.post(url, data=data, format="json", follow=True)

        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(response.status_code, 403)
