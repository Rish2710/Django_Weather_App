# Weather Alert Web Service

This Django-based web service allows users to retrieve real-time weather data for any city. The service provides detailed weather information, including temperature, humidity, wind speed, and weather conditions, along with alerts for extreme weather conditions like thunderstorms, hurricanes, or high temperatures.

## Features

- **Current Temperature**: Displays the current temperature in the city.
- **Highest Temperature**: Provides the highest temperature recorded in the city.
- **Lowest Temperature**: Provides the lowest temperature recorded in the city.
- **Humidity**: Displays the current humidity percentage.
- **Condition**: Shows the current weather condition (e.g., Rain, Clear, Snow).
- **Wind Speed**: Displays the current wind speed in meters per second (m/s).
- **Average Temperature (Last 24 Hours)**: Shows the average temperature over the past 24 hours.

### **Weather Alerts**
If the following conditions are met, an alert will be shown at the bottom of the report:
- **Thunderstorm** or **Hurricane** detected in the current weather condition.
- **Temperature exceeds 35°C**.

## How It Works

1. Enter the name of the city in the input field.(For multiple cities enter them comma-seperated.)
2. Submit the form to retrieve the current weather data for that city.
3. The service will display the following details:
    - Current Temperature: `23.5°C`
    - Highest Temperature: `23.8°C`
    - Lowest Temperature: `22.9°C`
    - Humidity: `89.0%`
    - Condition: `Rain`
    - Wind Speed: `3.09 m/s`
    - Average Temperature (last 24h): `23.5°C`
4. If extreme weather conditions (like a thunderstorm or hurricane) are detected or if the temperature exceeds 35°C, an alert message will appear below the weather information.

## Deployment

The web service is deployed at the following URL:

[Weather Alert Web Service](https://django-weather-app-0jl0.onrender.com/weather/)

Simply click the link and start checking the weather conditions for any city.

## Technologies Used

- **Django**: The backend web framework.
- **Bootstrap**: For responsive UI design.
- **OpenWeatherMap API**: For fetching real-time weather data.
