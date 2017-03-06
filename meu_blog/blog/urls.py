# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from . import views
#from blog.views import Artigo

urlpatterns = patterns(views, 
    url('^$', views.blog, name='blog'),
    #url('^$', views.blog, name='blog'),
)