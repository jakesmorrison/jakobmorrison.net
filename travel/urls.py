from django.conf.urls import url
from . import views

app_name= 'travel'
urlpatterns = [
    url(r'^$', views.home, name='home'),
]