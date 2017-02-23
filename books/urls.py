from django.conf.urls import url, include
from . import views

app_name = 'books'
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^quick_chart/$', views.quick_chart, name='quick_chart'),
    url(r'^vector_chart/$', views.vector_chart, name='vector_chart'),
    url(r'^all_book_vector_chart/$', views.all_book_vector_chart, name='all_book_vector_chart'),
]