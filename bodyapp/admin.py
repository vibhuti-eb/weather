from django.contrib import admin
from .models import CityRequest, WeatherResponse

# Register your models here.
admin.site.register(CityRequest)
admin.site.register(WeatherResponse)