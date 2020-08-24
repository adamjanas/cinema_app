from django.db import models
from app.users.models import User


class CreatedAtAbstractModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
