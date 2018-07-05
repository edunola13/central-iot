from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^devices/$', views.DeviceList.as_view()),
    url(r'^devices/type_sensors/$', views.devices_sensor), 
    url(r'^devices/type_actuators/$', views.devices_actuator),    
    url(r'^devices/(?P<pk>[0-9]+)/$', views.DeviceDetail.as_view()),
    url(r'^devices/(?P<pk>[0-9]+)/sensors/$', views.sensors_of_devices),
]