from django.contrib import admin
from .models import Genre, Director, Films
# Register your models here.

admin.site.register(Films)
admin.site.register(Director)
admin.site.register(Genre)