from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/(?P<username>[a-zA-Z]*)', views.login, name='login')
]