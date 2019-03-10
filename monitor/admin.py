from django.contrib import admin
from .models import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'has_controls', 'is_visiable']


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_visiable', 'control_type']


Models = (AlertCategory, AlertStatus, ProblemStatus, Unit, BodyType,
          Alert, Problem, ControlType)

admin.site.register(Models)
