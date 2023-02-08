from django.db import models
from devices.models import Devices

class Locations(models.Model):
    device_id = models.OneToOneField(Devices, on_delete=models.CASCADE, to_field='id', related_name='location_id', primary_key=True)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)

    @property
    def get_device_name(self):
        name = Devices.objects.filter(id=self.device_id).values_list('device_full_name')
        return name[0][0]
