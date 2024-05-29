from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
import json, urllib.request
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@csrf_exempt
def index(request):
    # return HttpResponse("Hello")

    if request.method == 'GET':
        city = request.GET.get('city')

        weatherLoad = urllib.request.urlopen(
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&appid=7a908ab52be0fcce27d79396efc4fcb4').read()
        
        weatherDict = json.loads(weatherLoad)

        weather = {
            "long": str(weatherDict['coord']['lon']),
            "lat" : str(weatherDict['coord']['lat']), 
            "temp": str(round(weatherDict['main']['temp'] -  273.15, 1) )+ '\xb0C', 
            "pressure": str(weatherDict['main']['pressure']), 
            "humidity": str(weatherDict['main']['humidity']), 
        }
    
    else:
        weather={}

    # return HttpResponse("Hello there!")
    return JsonResponse(weather)
