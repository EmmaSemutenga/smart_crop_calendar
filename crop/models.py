from django.db import models

# Create your models here.
class Crop(models.Model):
    name = models.CharField(max_length=100)
    agro_ecological_zone = models.CharField(max_length=100)
    season = models.CharField(max_length=100)
    early_sowing_month = models.PositiveBigIntegerField()
    late_sowing_month = models.PositiveBigIntegerField()
    sowing_value = models.CharField(max_length=100)
    sowing_unit = models.CharField(max_length=100)
    growing_period = models.CharField(max_length=100)
    water_needed = models.CharField(max_length=100, null=True, blank=True)
    challenges = models.TextField()

    def __str__(self):
        return self.name

class MonthlyPrecipitation(models.Model):
    district = models.CharField(max_length=20)
    jan = models.FloatField()
    feb = models.FloatField()
    mar = models.FloatField()
    apr = models.FloatField()
    may = models.FloatField()
    jun = models.FloatField()
    jul = models.FloatField()
    aug = models.FloatField()
    sept = models.FloatField()
    oct = models.FloatField()
    nov = models.FloatField()
    dec = models.FloatField()

    def __str__(self):
        return self.district

class SeasonalPrecipitation(models.Model):
    district = models.CharField(max_length=20)
    dec_jan_feb = models.FloatField()
    mar_apr_may = models.FloatField()
    jun_jul_aug = models.FloatField()
    sep_oct_nov = models.FloatField()

    def __str__(self):
        return self.district

class SeasonForecast:
    pass