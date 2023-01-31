from django.urls import path
from . import views, cam2

app_name = 'streams'

urlpatterns = [
    path('cam2', views.Cam2, name='cam2'),
    path('cam1', cam2.Cam1, name='cam1'),
]