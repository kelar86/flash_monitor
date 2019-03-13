from django.contrib import admin
from .models import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'has_controls', 'is_visiable']


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'is_visiable']


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    list_display = ['start_date', 'application', 'description', 'is_planed']
    filter_horizontal = ('control', 'unit', 'body_type')


@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['status', 'detection_date', 'application', 'description']
    filter_horizontal = ('control', 'unit', 'body_type')


Models = (
    AlertCategory,
    AlertStatus,
    ProblemStatus,
    Unit,
    BodyType)

admin.site.register(Models)
