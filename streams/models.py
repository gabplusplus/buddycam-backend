from django.db import models
from devices.models import Devices
from streams_switch.url_manager import set_url

class Streams(models.Model):
    device_id = models.OneToOneField(Devices, on_delete=models.CASCADE, to_field='id', related_name="device_id", primary_key=True)
    status = models.BooleanField(default=True)

    @property
    def get_url(self):
        url = Devices.objects.filter(id=self.device_id).values_list('device_ip')
        nam = Devices.objects.filter(id=self.device_id).values_list('device_full_name')
        dev_id = str(self.device_id)
        set_url(dev_id, url[0][0], nam[0][0])
        return url[0][0]
