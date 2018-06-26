from django.db import models

class Weather(models.Model):
    temperature = models.IntegerField()
    humidity = models.IntegerField()

    def __str__(self):
        return "T: " + str(temperature) + "°C"
