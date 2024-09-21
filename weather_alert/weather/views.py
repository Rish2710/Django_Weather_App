# weather/views.py
from django.shortcuts import redirect, render
from datetime import datetime
from django.utils import timezone
from datetime import timedelta
from .models import WeatherData
from django.db.models import Avg
from .services import fetch_weather_data

def store_weather_data(city):
    data = fetch_weather_data(city)
    if data:
        temperature_in_celsius = round(data['main']['temp'] - 273.15, 2)
        highest_temp = round(data['main']['temp_max'] - 273.15, 2)
        lowest_temp = round(data['main']['temp_min'] - 273.15, 2)
        weather_data = WeatherData.objects.create(
            city=data['name'],
            temperature=temperature_in_celsius,
            humidity=data['main']['humidity'],
            condition=data['weather'][0]['main'],
            wind_speed=data['wind']['speed'],
            highest_temp=highest_temp,
            lowest_temp=lowest_temp,
            last_updated=timezone.now()
        )
        weather_data.save()


def calculate_average_temperature(city):
    one_day_ago = timezone.now() - timedelta(hours=24)
    weather_records = WeatherData.objects.filter(city=city, last_updated__gte=one_day_ago)
    avg_temp = weather_records.aggregate(Avg('temperature'))['temperature__avg']
    return avg_temp

def check_extreme_weather(city):
    latest_data = WeatherData.objects.filter(city=city).last()
    if latest_data:
        if latest_data.temperature > 35 or latest_data.condition in ["Thunderstorm", "Hurricane"]:
            return f"Extreme weather alert in {city}: {latest_data.condition}"
        return None

from django.shortcuts import render, redirect
from .models import WeatherData

def weather_view(request):
    cities_weather = []
    if request.method == "POST":
        # Get the input city string from the user and split by commas
        city_input = request.POST.get('city')
        cities = city_input.split(',')
        cities = [city.strip() for city in cities if city.strip()]

        for city in cities:
            store_weather_data(city)
            latest_data = WeatherData.objects.filter(city=city).last()
            avg_temp = calculate_average_temperature(city)
            extreme_alert = check_extreme_weather(city)

            # Add the data for this city to the list
            if latest_data:
                cities_weather.append({
                    'city': latest_data.city,
                    'temperature': round(latest_data.temperature, 2),
                    'highest_temp': round(latest_data.highest_temp, 2),
                    'lowest_temp': round(latest_data.lowest_temp, 2),
                    'humidity': latest_data.humidity,
                    'condition': latest_data.condition,
                    'wind_speed': latest_data.wind_speed,
                    'avg_temp': round(avg_temp, 2),
                    'extreme_alert': extreme_alert
                })

        # Store the result in the session to access it after redirect
        request.session['cities_weather'] = cities_weather
        return redirect('weather_view')  # Redirect to the same view

    else:  # Handle GET requests
        # Retrieve weather data from the session
        cities_weather = request.session.get('cities_weather', [])

        # Clear the session data after using it
        if cities_weather:
            del request.session['cities_weather']

    return render(request, 'weather/weather_view.html', {
        'cities_weather': cities_weather
    })



# def weather_view(request):
#     cities_weather = []  # List to hold weather data for all cities

#     if request.method == "POST":
#         # Get the input city string from the user and split by commas
#         city_input = request.POST.get('city')
#         cities = city_input.split(',')  # Split by comma in case of multiple cities
#         cities = [city.strip() for city in cities if city.strip()]  # Remove any extra spaces and ignore empty strings

#         for city in cities:
#             store_weather_data(city)  # Fetch and store weather data for each city
#             latest_data = WeatherData.objects.filter(city=city).last()
#             avg_temp = calculate_average_temperature(city)
#             extreme_alert = check_extreme_weather(city)

#             # Add the data for this city to the list
#             if latest_data:
#                 cities_weather.append({
#                     'city': latest_data.city,
#                     'temperature': latest_data.temperature,
#                     'highest_temp': latest_data.highest_temp,
#                     'lowest_temp': latest_data.lowest_temp,
#                     'humidity': latest_data.humidity,
#                     'condition': latest_data.condition,
#                     'wind_speed': latest_data.wind_speed,
#                     'avg_temp': avg_temp,
#                     'extreme_alert': extreme_alert
#                 })

#         # Redirect to the same view with a GET request after processing
#         return redirect('weather_view')  # Make sure to use the correct URL name

#     else:  # GET request
#         # Optionally, you can fetch the latest weather data here if needed
#         # For now, this will handle the case when the user directly accesses the page
#         return render(request, 'weather/weather_view.html', {
#             'cities_weather': cities_weather
#         })


# # def weather_view(request):
# #     cities_weather = []  # List to hold weather data for all cities

# #     if request.method == "POST":
# #         # Get the input city string from the user and split by commas
# #         city_input = request.POST.get('city')
# #         cities = city_input.split(',')  # Split by comma in case of multiple cities
# #         cities = [city.strip() for city in cities if city.strip()]  # Remove any extra spaces and ignore empty strings

# #         for city in cities:
# #             store_weather_data(city)  # Fetch and store weather data for each city
# #             latest_data = WeatherData.objects.filter(city=city).last()
# #             avg_temp = calculate_average_temperature(city)
# #             extreme_alert = check_extreme_weather(city)

# #             # Add the data for this city to the list
# #             if latest_data:
# #                 cities_weather.append({
# #                     'city': latest_data.city,
# #                     'temperature': latest_data.temperature,
# #                     'highest_temp': latest_data.highest_temp,
# #                     'lowest_temp': latest_data.lowest_temp,
# #                     'humidity': latest_data.humidity,
# #                     'condition': latest_data.condition,
# #                     'wind_speed': latest_data.wind_speed,
# #                     'avg_temp': avg_temp,
# #                     'extreme_alert': extreme_alert
# #                 })

# #     return render(request, 'weather/weather_view.html', {
# #         'cities_weather': cities_weather
# #     })

