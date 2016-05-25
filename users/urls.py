from django.conf.urls import url, include

from . import views

app_name = 'users'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<username>[\w.@+-]+)/', include([
        url(r'^$', views.profile, name='profile'),
        url(r'^edit/$', views.edit_profile, name='edit_profile'),
    ])),
]