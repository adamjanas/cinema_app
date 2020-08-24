from django.db import models
from app.users.models import User
from django.urls import reverse
import datetime
from app.core.models import BaseAbstractModel, CreatedAtAbstractModel


class Advertisement(BaseAbstractModel, CreatedAtAbstractModel):
    pass


class Promotion(BaseAbstractModel, CreatedAtAbstractModel):
    pass


class Price(CreatedAtAbstractModel):
    name = models.CharField(max_length=50)
    value = models.DecimalField(max_digits=8, decimal_places=2)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.value}"

class Movie(BaseAbstractModel, CreatedAtAbstractModel):
    pass

    def __str__(self):
        return f"{self.name}"


class Hall(CreatedAtAbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    columns = models.PositiveSmallIntegerField(help_text='Select number of columns')
    rows = models.PositiveSmallIntegerField(help_text='Select number of rows')

    def __str__(self):
        return f"{self.name}"


class Show(CreatedAtAbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE, related_name='show_movies')
    hall = models.ForeignKey('Hall', on_delete=models.CASCADE, related_name='show_halls')
    date = models.DateTimeField(default=datetime.date.today())



