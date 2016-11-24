from django.conf.urls import url
from django.contrib import admin
from searchengine.views import *
urlpatterns = [
    url(r'^$', search),
]

