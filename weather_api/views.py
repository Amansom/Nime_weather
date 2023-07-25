# weather_api/views.py
import requests
from django.shortcuts import render

def home(request):
    return render(request, 'weather_api/home.html')

def get_weather(request):
    if request.method == 'POST':
        option = request.POST['option']
        date = request.POST['date']

        url = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
        response = requests.get(url)
        data = response.json()

        if option == '1':
            temperature = None
            for item in data["list"]:
                if item["dt_txt"].split()[0] == date:
                    temperature = item["main"]["temp"]
                    break
            result = f"Temperature on {date}: {temperature} Kelvin" if temperature else "No weather data available for the given date."

        elif option == '2':
            wind_speed = None
            for item in data["list"]:
                if item["dt_txt"].split()[0] == date:
                    wind_speed = item["wind"]["speed"]
                    break
            result = f"Wind Speed on {date}: {wind_speed} m/s" if wind_speed else "No weather data available for the given date."

        elif option == '3':
            pressure = None
            for item in data["list"]:
                if item["dt_txt"].split()[0] == date:
                    pressure = item["main"]["pressure"]
                    break
            result = f"Pressure on {date}: {pressure} hPa" if pressure else "No weather data available for the given date."

        elif option == '0':
            result = "Program terminated."

        else:
            result = "Invalid option."

        return render(request, 'weather_api/result.html', {'result': result})
