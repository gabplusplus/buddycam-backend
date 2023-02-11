from streams.models import Streams
from rest_framework import generics, permissions
from rest_framework_simplejwt import authentication
from .serializers import StreamsSerializer
from devices.models import Devices
from members.models import Members
from streams import views
from .url_manager import destroy
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from .url_manager import cam_list
import json
from rest_framework import status

def get_member_id(dev_id):
    member = Devices.objects.filter(id=dev_id).values_list('device_full_name')
    id = Members.objects.filter(full_name=member[0][0]).values_list('id')
    return id[0][0]

class StreamsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Streams.objects.all()
    serializer_class = StreamsSerializer

    def perform_create(self, serializer):
        current_entries = Streams.objects.count()
        if current_entries >=6:
            raise ValidationError("Limit reached. Disconnect other device")
        else:
            device_id = self.request.data.get('device_id')
            member_id = get_member_id(device_id)
            device = Devices.objects.get(id=device_id)
            member_status = Members.objects.get(id=member_id)
            device.status = member_status.is_connected = "Connected"
            device.save()
            member_status.save()
            serializer.save()

class StreamsDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Streams.objects.all()
    serializer_class = StreamsSerializer
    lookup_field = 'pk'

class StreamsDestroy(generics.DestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Streams.objects.all()
    serializer_class = StreamsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        destroy(str(instance.device_id))
        device = Devices.objects.get(id=instance.device_id)
        member = Members.objects.get(id=get_member_id(device))
        member.is_connected = device.status = "Disconnected"
        member.save()
        device.save()
        super().perform_destroy(instance)