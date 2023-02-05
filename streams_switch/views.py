from streams.models import Streams
from rest_framework import generics, permissions
from rest_framework_simplejwt import authentication
from .serializers import StreamsSerializer
from devices.models import Devices
from streams import views
from .url_manager import destroy
from rest_framework.serializers import ValidationError
from rest_framework.response import Response
from .url_manager import cam_list
import json

class StreamsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Streams.objects.all()
    serializer_class = StreamsSerializer

    def perform_create(self, serializer):
        current_entries = Streams.objects.count()
        if current_entries >=6:
            raise ValidationError("Limit reached. Disconnect other device")
        else:
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
        super().perform_destroy(instance)