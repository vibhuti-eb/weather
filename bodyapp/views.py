import timeit
import urllib.parse
from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest
import json, urllib.request
from django.views.decorators.csrf import csrf_exempt
from .models import CityRequest, WeatherResponse
from .validator import Validator

# Create your views here.

@csrf_exempt
def index(request):
    #Starting the Timer
    start = timeit.default_timer()

    if request.method == 'GET':
        city = request.GET.get('city')

        # Validating the input city name
        if Validator.cityParamValidator(city):
            print("Time Taken : " ,timeit.default_timer() - start)
            return HttpResponseBadRequest(JsonResponse({"message": "Invalid City name"}))

        #Saving the city requested in DB
        cityRequest = CityRequest(city = city)
        cityRequest.save()

        #Calling external endpoint
        weatherLoad = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + urllib.parse.quote(city) + '&appid=7a908ab52be0fcce27d79396efc4fcb4').read()
        
        #Converting the JSON response to Python Dictionary
        weatherDict = json.loads(weatherLoad)

        #Extracting necessary info from the dict
        weather = {
            "longitude": str(weatherDict['coord']['lon']),
            "latitude" : str(weatherDict['coord']['lat']), 
            "temperature": str(round(weatherDict['main']['temp'] -  273.15, 1) )+ '\xb0C', 
            "pressure": str(weatherDict['main']['pressure']), 
            "humidity": str(weatherDict['main']['humidity']), 
        }

        #Saving response to DB
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

    #Stopping the timer
    print("Time Taken : " ,timeit.default_timer() - start)
    return JsonResponse(weather)
