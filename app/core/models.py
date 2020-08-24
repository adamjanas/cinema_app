from django.db import models
from app.users.models import User


class CreatedAtAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class BaseAbstractModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    content = models.TextField()


    def __str__(self):
        return f"{self.name} - {self.author}"

    class Meta:
        abstract = True