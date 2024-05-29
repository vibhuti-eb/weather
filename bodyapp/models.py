from django.db import models

# Create your models here.
class CityRequest(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=100)

class WeatherResponse(models.Model):
    cityRequest = models.OneToOneField(
        CityRequest,
        on_delete=models.PROTECT,
        primary_key=True
    )
    longitude = models.CharField(max_length=10)
    latitude = models.CharField(max_length=10)
    temperature = models.CharField(max_length=5)
    pressure = models.CharField(max_length=10)
    humidity = models.CharField(max_length=10)
