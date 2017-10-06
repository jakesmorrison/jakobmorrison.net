from django.conf.urls import url
from . import views

app_name = 'heartbeat'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^investment_analyzer$', views.investment_analyzer, name='investment_analyzer'),
    url(r'^withdraw_analyzer$', views.withdraw_analyzer, name='withdraw_analyzer'),
    url(r'^demo_dashboard$', views.demo_dashboard, name='demo_dashboard'),
    url(r'^get_data$', views.get_data, name='get_data'),

]