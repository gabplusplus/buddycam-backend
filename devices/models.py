from django.db import models
import uuid
from members.models import Members

class Devices(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_ip = models.CharField(max_length=255)
    device_full_name = models.ForeignKey(Members, on_delete=models.CASCADE, to_field='full_name', related_name='deviceFullName')
    device_batt = models.CharField(max_length=3, default='0')
    device_signal = models.IntegerField(default=0)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)

    def __str__(self):
        dfn = str(self.device_full_name)
        di = str(self.device_ip)

        return f'{dfn} :: {di}'
