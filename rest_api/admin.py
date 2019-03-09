from .models import *
from django.contrib import admin


@admin.register(SearchResult)
class SearchResultAdmin(admin.ModelAdmin):
    list_display = ['user', 'date', 'search_object']


@admin.register(SearchObject)
class SearchObjectAdmin(admin.ModelAdmin):
    list_display = ['application', 'control', 'unit', 'body_type']
