from django.conf.urls import url
from . import views

app_name = 'poo'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_data/', views.add_data, name='add_data')
]