from django.contrib import admin

# Register your models here.
from .models import Farmer, ExtensionWorker, SentSMS

admin.site.register(Farmer)
admin.site.register(ExtensionWorker)
admin.site.register(SentSMS)