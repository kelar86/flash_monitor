"""
flash_monitor_project URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls)
]

if 'rest_api' in settings.INSTALLED_APPS:
    urlpatterns += [path(r'api/', include('rest_api.urls'))]
