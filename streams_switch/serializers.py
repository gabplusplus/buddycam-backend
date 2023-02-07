from rest_framework import serializers
from streams.models import Streams
from streams_switch.url_manager import has_none_value
from streams.models import Streams

# def validate_post_limit(data):
#     # retrieve current number of entries
#     current_entries = Streams.objects.count()
#     if current_entries >= 6:
#         raise serializers.ValidationError("Post limit reached. No more entries allowed.")
#     return data


class StreamsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streams
        fields = [
            'device_id',
            'status',
            'get_url',
            'get_device_name',
        ]

    def create(self, validated_data):
        return Streams.objects.create(**validated_data)
    
    # def validate(self, data):
    #     data = validate_post_limit(data)
    #     return data