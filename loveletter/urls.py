from django.conf.urls import url
from . import views

app_name = "loveletter"
urlpatterns = [
    url(r'^$', views.main_window, name='main_window'),
    url(r'game_init/', views.init_game, name='init_game'),
    url(r'join_game/', views.join_game, name='join_game'),
    url(r'game/', views.play_game, name='play_game'),
    url(r'refresh_status/', views.refresh_status, name='refresh_status'),
    url(r'deal/', views.deal, name='deal'),
    url(r'get_new_card/', views.get_new_card, name='get_new_card'),
    url(r'play_card/', views.play_card, name='play_card'),
]



