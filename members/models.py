from django.db import models
from django.utils import timezone

# from django_random_id_model import RandomIdModel

class Members(models.Model):
    full_name = models.CharField(max_length=256, unique=True)
    register_date = models.DateTimeField(default=timezone.now)
    is_connected = models.CharField(default="Disconnected", max_length=20)
    
    def __str__(self):
        return self.full_name