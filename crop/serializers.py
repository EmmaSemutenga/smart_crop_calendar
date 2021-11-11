from rest_framework import serializers
from .models import Crop, MonthlyPrecipitation, SeasonalPrecipitation

class CropSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Crop
        fields = '__all__'

class MonthlyPrecipitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MonthlyPrecipitation
        fields = '__all__'

class SeasonalPrecipitationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SeasonalPrecipitation
        fields = '__all__'