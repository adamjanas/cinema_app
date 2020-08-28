from django.urls import path
from django.conf.urls import url
from django.conf.urls import include
from app.clients.views import (
    BookingCreateView,
    BookingListView,
    BookingDeleteView,
    UserBookingListView,
    generate_pdf,
)

urlpatterns = [
    path('show/<int:pk>/book', BookingCreateView.as_view(), name='book-show'),
    path('booking-list', BookingListView.as_view(), name='booking-list'),
    path('booking/<int:pk>/delete', BookingDeleteView.as_view(), name='delete-booking'),
    path('booking/<str:username>/list', UserBookingListView.as_view(), name='my-reservations'),
    path('booking/<int:pk>/generate/pdf', generate_pdf, name='generate-pdf'),
]
