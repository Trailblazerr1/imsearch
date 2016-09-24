from django.shortcuts import render

# Create your views here.
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^search/$', views.search, name='search'),
    
    url(r'^pick/(?P<uid>/*.+)$',views.viewname, name='viewname'),
    url(r'^pick/$', views.pick, name='pick'),


]