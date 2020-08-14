from django.urls import path
from django.conf.urls import include
from app.structure.views import (
    home
)


urlpatterns = [
    path('', home, name='home')
]
