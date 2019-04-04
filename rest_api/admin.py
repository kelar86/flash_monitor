from .models import *
from django.contrib import admin


@admin.register(SearchAdvise)
class SearchAdviseAdmin(admin.ModelAdmin):
    list_display = ['schema']
