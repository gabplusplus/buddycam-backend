from rest_framework import serializers
from . import models
from .models import Devices 

class DevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Devices
        fields = '__all__'
    
    def create(self, validated_data):
        return Devices.objects.create(**validated_data)