from rest_framework import generics, permissions
from rest_framework_simplejwt import authentication
from .serializers import LocationsSerializer
from .models import Locations

class LocationsList(generics.ListCreateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer

    def perform_create(self, serializer):
        serializer.save()

class LocationsDetails(generics.RetrieveAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer
    lookup_field = 'pk'

class LocationsUpdate(generics.UpdateAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()

class LocationsDestroy(generics.DestroyAPIView):
    permission_classes = [permissions.AllowAny]
    queryset = Locations.objects.all()
    serializer_class = LocationsSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        super().perform_destroy(instance)