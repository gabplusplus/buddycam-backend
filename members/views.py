from rest_framework import generics, permissions as perm
from .models import Members
from .serializers import MembersSerializer
from rest_framework_simplejwt import authentication

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
        super().perform_destroy(instance)
