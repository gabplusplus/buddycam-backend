from django.urls import path
from .views import LocationsDetails, LocationsList, LocationsDestroy, LocationsUpdate

app_name = 'locations'

urlpatterns = [
    path('', LocationsList.as_view(), name='StreamsListCreate'),
    path('<str:pk>/', LocationsDetails.as_view(), name='StreamsDetails'),
    path('<str:pk>/delete/', LocationsDestroy.as_view(), name='StreamsDestroy'),
    path('<str:pk>/update/', LocationsUpdate.as_view(), name='membersupdate'),
]