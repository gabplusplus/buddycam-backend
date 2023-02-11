from django.urls import path
from .views import StreamsDetails, StreamsList, StreamsDestroy, StreamsDestroyAll

app_name = 'stream_switch'

urlpatterns = [
    path('', StreamsList.as_view(), name='StreamsListCreate'),
    path('<str:pk>/', StreamsDetails.as_view(), name='StreamsDetails'),
    path('<str:pk>/delete/', StreamsDestroy.as_view(), name='StreamsDestroy'),
]