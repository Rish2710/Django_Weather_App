import requests

WEATHER_API_KEY="0f3470bbf831e0c425e15028412dcd8f"
WEATHER_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city):
    url = f"{WEATHER_API_URL}?appid={WEATHER_API_KEY}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None