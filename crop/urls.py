from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it
router = DefaultRouter()
router.register(r'crop_calendar', views.CropViewSet)
router.register(r'seasonal_precipitation', views.SeasonalPrecipitationViewSet)
router.register(r'monthly_precipitation', views.MonthlyPrecipitationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

