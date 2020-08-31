import datetime

from django.db import models
from django.urls import reverse

from app.core.models import CreatedAtAbstractModel
from app.structure.models import Price, Seat, Show
from app.users.models import User


class Booking(CreatedAtAbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    ticket = models.ForeignKey(Price, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name="shows")

    def __str__(self):
        return f"{self.user} reservation"
