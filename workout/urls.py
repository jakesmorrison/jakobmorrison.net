from django.conf.urls import url
from . import views

app_name = 'workout'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'log/', views.log, name='log'),
    url(r'signup/', views.signup, name='signup'),
    url(r'change_type/', views.change_type, name='change_type'),
    url(r'add_to_db/', views.add_to_db, name='add_to_db'),
]