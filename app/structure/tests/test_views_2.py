import os

from app.structure.models import (Advertisement, Hall, Movie, Price, Promotion,
                                  Seat, Show)
from app.users.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse


class StructureTestCase(TestCase):

    client = Client()

    def setUp(self):
        self.client = Client()
        self.credentials = {
            "username": "testuser",
            "email": "test@test.com",
            "phone_number": 123123123,
            "role": 3,
            "password": "testpassword",
        }
        self.client.user = User.objects.create_user(**self.credentials)
        self.ad = Advertisement.objects.create(
            author=self.client.user, name="testname", content="testcontent"
        )
        self.promotion = Promotion.objects.create(
            author=self.client.user, name="testname", content="testcontent"
        )
        self.price = Price.objects.create(
            author=self.client.user, name="testname", value=2
        )
        self.hall = Hall.objects.create(author=self.client.user, name="testname")
        self.movie = Movie.objects.create(
            author=self.client.user, name="testname", content="testcontent"
        )
        self.show = Show.objects.create(
            author=self.client.user, movie=self.movie, hall=self.hall
        )
        self.seat = Seat.objects.create(author=self.client.user, row="A", column=5)

        self.ad_list = Advertisement.objects.all()
        self.promo_list = Promotion.objects.all()
        self.movie_list = Movie.objects.all()
        self.price_list = Price.objects.all()
        self.hall_list = Hall.objects.all()
        self.show_list = Show.objects.all()
        self.seat_list = Seat.objects.all()
        self.movie_1 = Movie.objects.get(name="testname")
        self.hall_1 = Hall.objects.get(name="testname")

    def test_ad_list(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("home")

        response = self.client.get(url)

        for model in self.ad_list:
            self.assertIn(model.name, response.content.decode())
            self.assertIn(model.content, response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/home.html")

    def test_ad_create(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("create-ad")

        data = {
            "author": self.client.user,
            "name": "testname",
            "content": "testcontent",
        }

        response = self.client.post(url, data=data, follow=True)

        self.assertTemplateUsed("app/ad_form.html")
        self.assertIn(data["name"], response.content.decode())
        self.assertIn(data["content"], response.content.decode())
        self.assertEqual(response.status_code, 200)

    def test_ad_delete(self):
        # deleting by overwriting GET method
        self.client.login(username="testuser", password="testpassword")

        url = reverse("delete-ad", args=(self.ad.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.ad in self.ad_list)

    def test_ad_update(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("update-ad", args=(self.ad.pk,))

        data = {"name": "testname - updated", "content": "testcontent- updated"}

        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/ad_form.html")
        self.assertIn(data["name"], response.content.decode())
        self.assertIn(data["content"], response.content.decode())

    def test_promotion_list(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("promo-list")

        response = self.client.get(url)

        for model in self.promo_list:
            self.assertIn(model.name, response.content.decode())
            self.assertIn(model.content, response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/promo_list.html")

    def test_promotion_create(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("create-promo")

        data = {
            "author": self.client.user,
            "name": "testname",
            "content": "testcontent",
        }

        response = self.client.post(url, data=data, follow=True)

        self.assertTemplateUsed("app/promo_form.html")
        self.assertIn(data["name"], response.content.decode())
        self.assertIn(data["content"], response.content.decode())
        self.assertEqual(response.status_code, 200)

    def test_promotion_delete(self):
        # deleting by overwriting GET method
        self.client.login(username="testuser", password="testpassword")

        url = reverse("delete-promo", args=(self.promotion.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.promotion in self.promo_list)

    def test_promotion_update(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("update-promo", args=(self.promotion.pk,))

        data = {"name": "testname - updated", "content": "testcontent- updated"}

        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/promo_form.html")
        self.assertIn(data["name"], response.content.decode())
        self.assertIn(data["content"], response.content.decode())

    def test_movie_list(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("movie-list")

        response = self.client.get(url)

        for model in self.movie_list:
            self.assertIn(model.name, response.content.decode())
            self.assertIn(model.content, response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/movie_list.html")

    def test_movie_create(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("create-movie")

        data = {
            "author": self.client.user,
            "name": "testname",
            "content": "testcontent",
        }

        response = self.client.post(url, data=data, follow=True)

        self.assertTemplateUsed("app/movie_form.html")
        self.assertIn(data["name"], response.content.decode())
        self.assertIn(data["content"], response.content.decode())
        self.assertEqual(response.status_code, 200)

    def test_movie_delete(self):
        # deleting by overwriting GET method
        self.client.login(username="testuser", password="testpassword")

        url = reverse("delete-movie", args=(self.movie.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.movie in self.movie_list)

    def test_movie_update(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("update-movie", args=(self.movie.pk,))

        data = {"name": "testname - updated", "content": "testcontent- updated"}

        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/movie_form.html")
        self.assertIn(data["name"], response.content.decode())
        self.assertIn(data["content"], response.content.decode())

    def test_price_list(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("price-list")

        response = self.client.get(url)

        for model in self.price_list:
            self.assertIn(model.name, response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/price_list.html")

    def test_price_create(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("create-price")

        data = {
            "author": self.client.user,
            "name": "testname",
            "value": "2",
        }

        response = self.client.post(url, data=data, follow=True)

        self.assertTemplateUsed("app/price_form.html")
        self.assertIn(data["name"], response.content.decode())
        self.assertIn(data["value"], response.content.decode())
        self.assertEqual(response.status_code, 200)

    def test_price_delete(self):
        # deleting by overwriting GET method
        self.client.login(username="testuser", password="testpassword")

        url = reverse("delete-price", args=(self.price.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.price in self.price_list)

    def test_price_update(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("update-price", args=(self.price.pk,))

        data = {"name": "testname - updated", "value": "5"}

        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/price_form.html")
        self.assertIn(data["name"], response.content.decode())
        self.assertIn(data["value"], response.content.decode())

    def test_hall_list(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("hall-list")

        response = self.client.get(url)

        for model in self.hall_list:
            self.assertIn(model.name, response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/hall_list.html")

    def test_hall_create(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("create-hall")

        data = {
            "author": self.client.user,
            "name": "testname",
        }

        response = self.client.post(url, data=data, follow=True)

        self.assertTemplateUsed("app/hall_form.html")
        self.assertIn(data["name"], response.content.decode())
        self.assertEqual(response.status_code, 200)

    def test_hall_delete(self):
        # deleting by overwriting GET method
        self.client.login(username="testuser", password="testpassword")

        url = reverse("delete-hall", args=(self.hall.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.hall in self.hall_list)

    def test_hall_update(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("update-hall", args=(self.hall.pk,))

        data = {
            "author": self.client.user,
            "name": "testname - updated",
        }

        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/hall_form.html")
        self.assertIn(data["name"], response.content.decode())

    def test_seat_list(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("seat-list")

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/seat_list.html")

    def test_seat_create(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("create-seat")

        data = {"author": self.client.user, "row": "A", "column": 2}

        response = self.client.post(url, data=data, follow=True)

        self.assertTemplateUsed("app/seat_form.html")
        self.assertIn(data["row"], response.content.decode())
        self.assertEqual(response.status_code, 200)

    def test_seat_delete(self):
        # deleting by overwriting GET method
        self.client.login(username="testuser", password="testpassword")

        url = reverse("delete-seat", args=(self.seat.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.seat in self.seat_list)

    def test_seat_update(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("update-seat", args=(self.seat.pk,))

        data = {"author": self.client.user, "row": "A", "column": 2}

        response = self.client.post(url, data=data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/seat_form.html")

    def test_show_list(self):
        self.client.login(username="testuser", password="testpassword")
        url = reverse("show-list")

        response = self.client.get(url)

        for model in self.hall_list:
            self.assertIn(model.name, response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/show_list.html")

    def test_show_create(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("create-show")

        data = {
            "author": self.client.user,
            "movie": self.movie_1.pk,
            "hall": self.hall_1.pk,
        }

        response = self.client.post(url, data=data, follow=True)

        self.assertTemplateUsed("app/show_form.html")
        self.assertEqual(response.status_code, 200)

    def test_show_delete(self):
        # deleting by overwriting GET method
        self.client.login(username="testuser", password="testpassword")

        url = reverse("delete-show", args=(self.show.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.show in self.show_list)

    def test_show_update(self):
        self.client.login(username="testuser", password="testpassword")

        url = reverse("update-show", args=(self.show.pk,))

        data = {
            "author": self.client.user,
            "movie": self.movie_1.pk,
            "hall": self.hall_1.pk,
        }

        response = self.client.put(url, data=data, follow=True, format="json")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed("app/show_form.html")
