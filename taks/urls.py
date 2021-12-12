from django.urls import path
from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    url(r'^send_command$', views.download_posts, name='download'),
    path('', views.index, name='index'),
]
