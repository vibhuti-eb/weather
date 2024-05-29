from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json, urllib.request
from django.views.decorators.csrf import csrf_exempt
from .models import CityRequest, WeatherResponse

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'GET':
        city = request.GET.get('city')
        cityRequest = CityRequest(city = city)
        cityRequest.save()

        weatherLoad = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&appid=7a908ab52be0fcce27d79396efc4fcb4').read()
        
        weatherDict = json.loads(weatherLoad)

        weather = {
            "longitude": str(weatherDict['coord']['lon']),
            "latitude" : str(weatherDict['coord']['lat']), 
            "temperature": str(round(weatherDict['main']['temp'] -  273.15, 1) )+ '\xb0C', 
            "pressure": str(weatherDict['main']['pressure']), 
            "humidity": str(weatherDict['main']['humidity']), 
        }

        weatherResponse = WeatherResponse(
            cityRequest = cityRequest,
            longitude = weather.get("longitude"),
            latitude = weather.get("latitude"),
            temperature = weather.get("temperature"),
            pressure = weather.get("pressure"),
            humidity = weather.get("humidity")
        )
        weatherResponse.save()
    
    else:
        weather={}

    # return HttpResponse("Hello there!")
    return JsonResponse(weather)
