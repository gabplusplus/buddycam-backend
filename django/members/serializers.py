from rest_framework import serializers
from .models import Members

class MembersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Members
        fields = (
            'id',
            'full_name',
            'register_date',
            'is_connected',
            'device_ip',
        )
