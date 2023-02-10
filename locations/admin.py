from django.contrib import admin
from .models import Locations

@admin.register(Locations)
class LocationsAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'lat', 'long')
