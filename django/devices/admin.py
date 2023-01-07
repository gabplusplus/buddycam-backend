from django.contrib import admin
from . import models

@admin.register(models.Devices)
class DevicesAdmin(admin.ModelAdmin):
    list_display = ('device_full_name', 'device_ip', 'device_batt', 'device_signal', 'lat', 'long')
