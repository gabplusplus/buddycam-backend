from django.db import models
from shortuuid.django_fields import ShortUUIDField
from members.models import Members

class Devices(models.Model):
    id = ShortUUIDField(primary_key=True, length=8, editable=False)
    device_ip = models.CharField(max_length=255, unique=True)
    device_full_name = models.ForeignKey(Members, on_delete=models.CASCADE, to_field='full_name', related_name='deviceFullName')
    device_batt = models.CharField(max_length=3, default='0')
    device_signal = models.IntegerField(default=0)
    lat = models.FloatField(default=0)
    long = models.FloatField(default=0)
    is_connected = models.BooleanField(default=False)

    def __str__(self):
        return self.id
