from django.conf.urls import url
from . import views

app_name = 'resume'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^developer/', views.developer, name='developer'),
    url(r'^apps/', views.applications, name='applications'),
]
