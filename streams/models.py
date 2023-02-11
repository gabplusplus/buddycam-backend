from django.db import models
from devices.models import Devices
from streams_switch.url_manager import set_url
from .locations import long_value, lat_value

class Streams(models.Model):
    device_id = models.OneToOneField(Devices, on_delete=models.CASCADE, to_field='id', related_name="device_id", primary_key=True)
    long = models.CharField(default=long_value, max_length=150)
    lat = models.CharField(default=lat_value, max_length=150)

    @property
    def get_url(self):
        url = Devices.objects.filter(id=self.device_id).values_list('device_ip')
        name = Devices.objects.filter(id=self.device_id).values_list('device_full_name')
        dev_id = str(self.device_id)
        set_url(dev_id, url[0][0], name[0][0])
        return url[0][0]

    def get_device_name(self):
        name = Devices.objects.filter(id=self.device_id).values_list('device_full_name')
        return name[0][0]

    def status(self):
        return "Connected"