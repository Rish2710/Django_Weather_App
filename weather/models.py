from django.db import models

class WeatherData(models.Model):
    city = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    condition = models.CharField(max_length=50)
    wind_speed = models.FloatField()
    highest_temp = models.FloatField(null=True)
    lowest_temp = models.FloatField(null=True)
    last_updated = models.DateTimeField()

    def __str__(self):
        return self.city
