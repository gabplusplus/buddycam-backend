from rest_framework import generics, permissions
from .models import Devices
from rest_framework_simplejwt import authentication
from .serializers import DevicesSerializer
from streams_switch.url_manager import destroy

class DeviceList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer

    def perform_create(self, serializer):
        serializer.save()

class DeviceDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer
    lookup_field = 'pk'

class DeviceUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

class DeviceDestroy(generics.DestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Devices.objects.all()
    serializer_class = DevicesSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        print(str(instance.id))
        destroy(str(instance.id))
        super().perform_destroy(instance)