# from django.db import models


# class WeatherData(models.Model):
#     city = models.CharField(max_length=100)
#     temperature = models.FloatField()
#     humidity = models.IntegerField()
#     condition = models.CharField(max_length=100)
#     wind_speed = models.FloatField()
#     last_updated = models.DateTimeField()

#     def __str__(self):
#         return f"Weather in {self.city} at {self.last_updated}"


# weather/models.py

from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    condition = models.CharField(max_length=50)
    wind_speed = models.FloatField()
    highest_temp = models.FloatField(null=True)  # Highest temperature of the day
    lowest_temp = models.FloatField(null=True)   # Lowest temperature of the day
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.city
