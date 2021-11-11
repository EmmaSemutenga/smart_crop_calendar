from django.shortcuts import render
import crop
from rest_framework import viewsets
from .models import Crop, MonthlyPrecipitation, SeasonalPrecipitation
from .serializers import CropSerializer, MonthlyPrecipitationSerializer, SeasonalPrecipitationSerializer

# Create your views here.
# goal, is to demostrate the smart calender
#requirements
# scale down on one crop from sowing to haverst
# amount of water needed by that crop
# get season weather forecast and collerate with amount of water needed
#crop calendar with rainfall data/ https://www.fao.org/3/s2022e/s2022e02.htm
# farmers or extension workers to be notified using sms etc with advise and recomendation
# other apps to utilise our api
# dashboard for other partners
# other factors to consider: Evaporation
# https://climateknowledgeportal.worldbank.org/download-data
# disease control prevention and pests

class CropViewSet(viewsets.ModelViewSet):
    queryset = Crop.objects.all()
    serializer_class = CropSerializer

class MonthlyPrecipitationViewSet(viewsets.ModelViewSet):
    queryset = MonthlyPrecipitation.objects.all()
    serializer_class = MonthlyPrecipitationSerializer

class SeasonalPrecipitationViewSet(viewsets.ModelViewSet):
    queryset = SeasonalPrecipitation.objects.all()
    serializer_class = SeasonalPrecipitationSerializer