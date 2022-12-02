from django.db import models
from django.utils import timezone

# from django_random_id_model import RandomIdModel

class Members(models.Model):
    full_name = models.CharField(max_length=256)
    register_date = models.DateTimeField(default=timezone.now)
    is_connected = models.BooleanField(default=False)
    device_ip = models.GenericIPAddressField(default='0.0.0.0')

    def __str__(self):
        return self.full_name 
