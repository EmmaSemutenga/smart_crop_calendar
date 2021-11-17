from django.db import models
from .helpers import SMS

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

class SentSMS(models.Model):
    number = models.CharField(max_length=20, null=True, blank=True)
    status = models.CharField(max_length=20, null=True, blank=True)
    status_code = models.IntegerField()
    sent_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.number} -- {self.status}"

class Farmer(models.Model):
    district = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.phone_number

    def save(self):
        crops = set(Crop.objects.filter(agro_ecological_zone__contains=self.district).values_list('name'))
        recommended_crops = ''
        for crop in crops:
            recommended_crops += f"{crop[0]}, "

        my_sms = SMS()
        response = my_sms.send(self.phone_number, recommended_crops, self.phone_number)

        # response from sms api about sent status
        for recipient in response['SMSMessageData']['Recipients']:
            number = recipient['number']
            status = recipient['status']
            statusCode = recipient['statusCode']
            SentSMS.objects.create(number=number, status=status, status_code=statusCode)

        return super().save()




class ExtensionWorker(models.Model):
    name = models.CharField(max_length=20)
    district = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def save(self):
        crops = set(Crop.objects.filter(agro_ecological_zone__contains=self.district).values_list('name'))
        recommended_crops = ''
        for crop in crops:
            recommended_crops += f"{crop[0]}, "

        my_sms = SMS()
        response = my_sms.send(self.name, recommended_crops, self.phone_number)

        # response from sms api about sent status
        for recipient in response['SMSMessageData']['Recipients']:
            number = recipient['number']
            status = recipient['status']
            statusCode = recipient['statusCode']
            SentSMS.objects.create(number=number, status=status, status_code=statusCode)

        return super().save()

