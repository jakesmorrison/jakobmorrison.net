from django.conf.urls import url
from . import views

app_name= 'travel'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^euro', views.euro, name='euro'),
    url(r'^general$', views.general, name='general'),
    url(r'^sleep$', views.sleep, name='sleep'),
    url(r'^media$', views.media, name='media'),
    url(r'^transportation$', views.transportation, name='transportation'),
    url(r'^other$', views.other, name='other'),
    url(r'^food$', views.food, name='food'),

]