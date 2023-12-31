from rest_framework import generics, permissions as perm
from .models import Members
from .serializers import MembersSerializer
from rest_framework_simplejwt import authentication
from streams_switch.url_manager import destroy
from devices.models import Devices

# Members List and Create View
class MembersList(generics.ListCreateAPIView):
    permission_classes = [perm.AllowAny]
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

    def perform_create(self, serializer):
        serializer.save()

# Members Retrieve View
class MembersDetail(generics.RetrieveAPIView):
    permission_classes = [perm.AllowAny]
    queryset = Members.objects.all()
    serializer_class = MembersSerializer

# Members Update View
class MembersUpdate(generics.UpdateAPIView):
    permission_classes = [perm.AllowAny]
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        serializer.save()
    

# Members Destroy View
class MembersDestroy(generics.DestroyAPIView):
    permission_classes = [perm.AllowAny]
    queryset = Members.objects.all()
    serializer_class = MembersSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        if(Devices.objects.filter(device_full_name=instance.full_name).exists()):
            dev_id = Devices.objects.filter(device_full_name=instance.full_name).values_list('id')
            dev_id = dev_id[0][0]
            destroy(str(dev_id))
        super().perform_destroy(instance)
