from django.db import models
from app.users.models import User
from django.urls import reverse
import datetime
from app.core.models import CreatedAtAbstractModel
from app.core.constants import SeatRowE
from django.core.validators import MaxValueValidator, MinValueValidator


class BaseAbstractModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.author}"

    class Meta:
        abstract = True


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

    def __str__(self):
        return f"{self.name}"


class Seat(CreatedAtAbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    row = models.CharField(max_length=1, choices=SeatRowE.choices())
    column = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(6)],
        help_text='Column (1-6)')

    def __str__(self):
        return f"{self.row}{self.column}"


class Show(CreatedAtAbstractModel):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(
        'Movie',
        on_delete=models.CASCADE,
        related_name='movies')
    hall = models.ForeignKey(
        'Hall',
        on_delete=models.CASCADE,
        related_name='halls')
    date = models.DateTimeField(default=datetime.date.today())

    def __str__(self):
        return f"{self.movie} show"
