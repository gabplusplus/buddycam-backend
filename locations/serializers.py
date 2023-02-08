from rest_framework import serializers
from .models import Locations

class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locations
        fields = [
            'device_id',
            'lat',
            'long',
            'get_device_name',
        ]

    def create(self, validated_data):
        return Locations.objects.create(**validated_data)