from django.contrib import admin
from .models import *


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'has_controls', 'is_visiable']


class ControlAdmin(admin.ModelAdmin):
    list_display = ['name', 'icon', 'is_visiable']


Models = (AlertCategory, AlertStatus, ProblemStatus, Unit, BodyType,
          Alert, Problem)

admin.site.register(Application, ApplicationAdmin)
admin.site.register(Control, ControlAdmin)
admin.site.register(Models)
