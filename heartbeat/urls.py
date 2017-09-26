from django.conf.urls import url
from . import views

app_name = 'heartbeat'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^investment_analyzer$', views.investment_analyzer, name='investment_analyzer'),
    url(r'^withdraw_analyzer$', views.withdraw_analyzer, name='withdraw_analyzer'),

]