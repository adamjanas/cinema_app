from app.structure.models import (Advertisement, Hall, Movie, Price, Promotion,
                                  Show)
from django.contrib import admin

admin.site.register(Advertisement)
admin.site.register(Promotion)
admin.site.register(Price)
admin.site.register(Hall)
admin.site.register(Movie)
admin.site.register(Show)
