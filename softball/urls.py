from django.conf.urls import url
from . import views

app_name = 'softball'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'index_updates/', views.index_updates, name='index_updates'),
    url(r'change_season/', views.change_season, name='change_season'),
    url(r'player_dash/', views.player_dash, name='player_dash'),
    url(r'submit_poll/', views.submit_poll, name='submit_poll'),
    url(r'poll_chart/', views.poll_chart, name='poll_chart'),
    url(r'consistency/', views.consistency, name='consistency'),
    url(r'^api/$', views.all_stats),
]