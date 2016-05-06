from django.conf.urls import url

from . import views

app_name = 'projects'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<project_id>[0-9]+)/$', views.show, name='show'),
]