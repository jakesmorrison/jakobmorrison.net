from django.conf.urls import url
from . import views

app_name = 'softball'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'index_updates/', views.index_updates, name='index_updates'),
    url(r'change_season/', views.change_season, name='change_season'),
]