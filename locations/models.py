from django.db import models
from streams.models import Streams
from devices.models import Devices

class Locations(models.Model):
    device_id = models.OneToOneField(Streams, on_delete=models.CASCADE, to_field='device_id', related_name='location_id', primary_key=True)
    lat = models.CharField(max_length=255)
    long = models.CharField(max_length=255)

    def device_name(self):
        return self.device_id.get_device_name()