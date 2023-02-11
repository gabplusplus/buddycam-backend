from rest_framework import serializers
from . import models
from .models import Devices 

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Devices
        fields = [
            'id',
            'device_ip',
            'device_full_name',
            'lat',
            'long',
        ]
    
    def create(self, validated_data):
        return Devices.objects.create(**validated_data)