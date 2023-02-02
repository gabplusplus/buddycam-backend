from django.urls import path
from . import views

app_name = 'streams'

urlpatterns = [
    path('cam1', views.Cam1, name='cam1'),
    path('cam2', views.Cam2, name='cam2'),
    path('cam3', views.Cam3, name='cam3'),
    path('cam4', views.Cam4, name='cam4'),
    path('cam5', views.Cam5, name='cam5'),
    path('cam6', views.Cam6, name='cam6'),
]