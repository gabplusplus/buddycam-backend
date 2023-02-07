from django.contrib import admin

from streams.models import Streams

@admin.register(Streams)
class StreamsAdmin(admin.ModelAdmin):
    list_display = ('device_id', 'status')