from django.urls import path
from .views import CustomUserCreateView, BlacklistTokenUpdateView, UserLoginView

app_name = 'users'

urlpatterns = [
    path('create/', CustomUserCreateView.as_view(), name="create_user"),
    path('logout/blacklist/', BlacklistTokenUpdateView.as_view(),
         name='blacklist'),
    path('login/', UserLoginView.as_view(), name="login"),
]
