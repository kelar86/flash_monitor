from django.contrib import admin
from .models import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'has_controls', 'is_visiable']


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'is_visiable']


Models = (AlertCategory, AlertStatus, ProblemStatus, Unit, BodyType,
          Alert, Problem)

admin.site.register(Models)
