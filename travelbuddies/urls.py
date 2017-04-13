from django.conf.urls import url
from . import views

app_name="travelbuddies"
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'log/', views.log, name='log'),
    url(r'signup/', views.signup, name='signup'),
]