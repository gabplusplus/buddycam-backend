from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from .serializers import CustomUserSerializer, EditUserSerializer, ResetPasswordSerializer

from rest_framework import generics
from .models import NewUser

class UserLoginView(TokenObtainPairView):
    serializer_class = TokenObtainPairSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        if response.status_code == 200:
            user = get_user_model().objects.get(email=request.data['email'])
            response.data['id'] = user.id
            response.data['user_name'] = user.user_name
            response.data['email'] = user.email
            response.data['first_name'] = user.first_name
            response.data['last_name'] = user.last_name
        return response

class EditUserView(generics.RetrieveUpdateAPIView):
    queryset = NewUser.objects.all()
    serializer_class = EditUserSerializer

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class CustomUserCreateView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = NewUser.objects.all()

class BlacklistTokenUpdateView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
class ResetPasswordView(generics.UpdateAPIView):
    serializer_class = ResetPasswordSerializer
    queryset = NewUser.objects.all()
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        instance.set_password(serializer.validated_data['password'])
        instance.save()
        return Response({"message": "Password has been reset successfully."})