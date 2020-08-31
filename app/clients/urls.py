from app.clients.views import (BookingCreateView, BookingDeleteView,
                               BookingListView, UserBookingListView,
                               generate_pdf)
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path("show/<int:pk>/book", BookingCreateView.as_view(), name="book-show"),
    path("booking-list", BookingListView.as_view(), name="booking-list"),
    path("booking/<int:pk>/delete", BookingDeleteView.as_view(), name="delete-booking"),
    path(
        "booking/<str:username>/list",
        UserBookingListView.as_view(),
        name="my-reservations",
    ),
    path("booking/<int:pk>/generate/pdf", generate_pdf, name="generate-pdf"),
]
