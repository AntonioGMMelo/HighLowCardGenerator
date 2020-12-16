from django.conf.urls import url
from . import views
# (. significa que importa views da mesma directoria)
from django.urls import path

urlpatterns = [
    url(r'game', views.game, name='game'),
    url(r'settings', views.settings, name='settings'),
]
