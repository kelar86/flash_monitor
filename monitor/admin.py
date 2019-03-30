from django.contrib import admin
from .models import *
from django.forms import ModelForm
from django.conf import settings

import logging
logger = logging.getLogger(__name__)


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'has_controls', 'is_visiable']


@admin.register(Control)
class ControlAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'is_visiable']


class AlertAdminForm(ModelForm):
    list_display = ['start_date', 'application',
         'description', 'is_planed', 'category']
    filter_horizontal = ('control', 'unit', 'body_type')

    class Media:
        js = ('monitor/alert_admin_form.js',)


@admin.register(Alert)
class AlertAdmin(admin.ModelAdmin):
    form = AlertAdminForm



@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    list_display = ['status', 'detection_date', 'application', 'description']
    filter_horizontal = ('control', 'unit', 'body_type')


Models = (
    AlertCategory,
    AlertStatus,
    ProblemStatus,
    Unit,
    BodyType,
    ControlType)

admin.site.register(Models)
