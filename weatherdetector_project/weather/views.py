from django.contrib.sites import requests
from django.shortcuts import render
import json
import urllib.request

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']

        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city +
                                     '&appid=[API KEY]').read()  # Gets the data from the
        # openweathermap API. appid is the personal API key provided by openweathermap.

        json_data = json.loads(res)

        data = {  # Converts json data into python dictionary for easier manipulation
            "country_code": str(json_data['sys']['country']),
            "latitude": str(json_data['coord']['lat']),
            "longitude": str(json_data['coord']['lon']),
            'description': str(json_data['weather'][0]['description']).upper(),
            "temp": str((json_data['main']['temp']) - 273.15),
            "temp_min": str((json_data['main']['temp_min']) - 273.15),
            "temp_max": str((json_data['main']['temp_max']) - 273.15),
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
            "wind_speed": str(json_data['wind']['speed']),
            'icon': json_data['weather'][0]['icon']
        }

    else:
        city = ''
        data = {}
    return render(request, 'index.html', {'city': city, 'data': data})


