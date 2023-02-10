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
    path('cam1_1', views.Cam1_1, name='cam1'),
    path('cam2_2', views.Cam2_2, name='cam2'),
    path('cam3_3', views.Cam3_3, name='cam3'),
    path('cam4_4', views.Cam4_4, name='cam4'),
    path('cam5_5', views.Cam5_5, name='cam5'),
    path('cam6_6', views.Cam6_6, name='cam6'),
    path('list/', views.camlist, name="camlist"),
]