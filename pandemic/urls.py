from django.conf.urls import url
from . import views

app_name = "epidmeic"
urlpatterns = [
    url(r'^$', views.start, name='start'),
]