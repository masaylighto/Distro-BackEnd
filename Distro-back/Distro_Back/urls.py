"""
UrukProject URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
"""


from django.contrib import admin
from django.db import router
from django.urls import  include, path

from rest_framework import routers
from polls import api_endpoints




router = routers.DefaultRouter()

router.register('translations',api_endpoints.Translations_Set)
router.register('links',api_endpoints.links_Set)
router.register('features',api_endpoints.Features_Set)
router.register('distro',api_endpoints.Distro_Set)

urlpatterns = [
    
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    
]
