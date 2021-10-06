from django.db import models

# Create your models here.
class Temperature(models.Model):
    reading = models.FloatField()
    time_recorded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Temp reading: {self.reading} on {self.time_recorded}"