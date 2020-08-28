import os
from app.users.models import User
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from app.clients.models import Booking
from app.structure.models import (
    Advertisement,
    Promotion,
    Price,
    Hall,
    Movie,
    Show,
    Seat,
)


class ClientTestCase(TestCase):

    client = Client()

    def setUp(self):
        self.client = Client()
        self.credentials = {
            'username': 'testuser',
            'email': 'test@test.com',
            'phone_number': 123123123,
            'role': 3,
            'password': 'testpassword',
        }
        self.client.user = User.objects.create_user(**self.credentials)
        self.ticket = Price.objects.create(author=self.client.user, name='testname', value=4)
        self.seat = Seat.objects.create(author=self.client.user, row='A', column=2)
        self.hall = Hall.objects.create(author=self.client.user, name='testname')
        self.movie = Movie.objects.create(author=self.client.user, name='testname', content='testcontent')
        self.show = Show.objects.create(author=self.client.user, movie=self.movie, hall=self.hall)
        self.booking = Booking.objects.create(user=self.client.user, name='testname', surname='testname',
                                              ticket=self.ticket, seat=self.seat, show=self.show)

        self.booking_1 = Booking.objects.get(name='testname')
        self.booking_list = Booking.objects.all()

    def test_booking_list(self):
        self.client.login(username='testuser', password='testpassword')
        url = reverse('booking-list')

        response = self.client.get(url)

        for model in self.booking_list:
            self.assertIn(model.name, response.content.decode())
            self.assertIn(model.surname, response.content.decode())
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('app/booking_list.html')

    def test_booking_create(self):
        self.client.login(username='testuser', password='testpassword')

        url = reverse('book-show', args=(self.show.pk,))

        data = {
            'author': self.client.user,
            'name': 'testname',
            'surname': 'testsurname',
            'ticket': self.ticket,
            'seat': self.seat,
            'show': self.show

        }

        response = self.client.post(url, data=data, follow=True)

        self.assertTemplateUsed('app/booking_form.html')
        self.assertIn(data['name'], response.content.decode())
        self.assertIn(data['surname'], response.content.decode())
        self.assertEqual(response.status_code, 200)

    def test_booking_delete(self):
        # deleting by overwriting GET method
        self.client.login(username='testuser', password='testpassword')

        url = reverse('delete-booking', args=(self.booking.pk,))

        response = self.client.get(url, follow=True)

        self.assertEqual(response.status_code, 200)
        self.assertFalse(self.booking in self.booking_list)
