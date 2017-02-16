from django.conf.urls import url, include
from . import views

# from rest_framework import routers
# router = routers.DefaultRouter()
# router.register(r'words', views.WordsViewSet)
# url(r'^api/', include(router.urls)),
# url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

app_name = "definitions"
urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^add_to_db/', views.add_to_db, name='add_to_db'),
    url(r'^api/$', views.words_list),
    url(r'^api/current/$', views.words_current),
    url(r'^api/(?P<pk1>.*)=(?P<pk2>.*)$', views.words_detail),
]
