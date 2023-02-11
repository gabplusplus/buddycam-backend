from django.db import models
from shortuuid.django_fields import ShortUUIDField
from members.models import Members
from streams.locations import long_value, lat_value

class Devices(models.Model):
    id = ShortUUIDField(primary_key=True, length=8, editable=False)
    device_ip = models.CharField(max_length=255, unique=True)
    device_full_name = models.ForeignKey(Members, on_delete=models.CASCADE, to_field='full_name', related_name='deviceFullName')
    long = models.CharField(default=long_value, max_length=150)
    lat = models.CharField(default=lat_value, max_length=150)
    status = models.CharField(default="Disconnected", max_length=25)

    def __str__(self):
        return self.id
