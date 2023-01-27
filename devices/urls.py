from django.urls import path
from . import views as v

app_name = 'devices'

urlpatterns = [
    path('', v.DeviceList.as_view(), name='DevicesListCreate'),
    path('<str:pk>/', v.DeviceDetails.as_view(), name='DevicesDetails'),
    path('<str:pk>/update/', v.DeviceUpdate.as_view(), name='DevicesUpdate'),
    path('<str:pk>/delete/', v.DeviceDestroy.as_view(), name='DevicesDestroy'),
]

