from django.conf.urls import url, include

from . import views

app_name = 'projects'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<slug>[\w-]+)/', include([
        url(r'^$', views.details, name='details'),
        url(r'^join/$', views.join, name='join'),
    ])),
]