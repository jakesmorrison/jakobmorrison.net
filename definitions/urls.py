from django.conf.urls import url
from . import views

app_name = "definitions"
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add_to_db/', views.add_to_db, name='add_to_db'),
]
