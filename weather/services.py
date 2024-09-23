import requests
from decouple import config


WEATHER_API_KEY = config("WEATHER_API_KEY")
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    url = f"{WEATHER_API_URL}?appid={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None