from django.urls import path
from .views import CustomUserCreateView, BlacklistTokenUpdateView, UserLoginView, EditUserView, ResetPasswordView

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreateView.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('login/', UserLoginView.as_view(), name="login"),
    path('edit/<int:pk>/', EditUserView.as_view(), name="edit_user"),
    path('resetpass/<int:pk>/', ResetPasswordView.as_view(), name="reset"),
]
