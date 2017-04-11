from django.conf.urls import url
from . import views

app_name = 'map'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^get_long_lat/', views.get_long_lat, name='get_long_lat'),
    url(r'^send_long_lat/', views.send_long_lat, name='send_long_lat'),
]
