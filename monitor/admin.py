from django.contrib import admin
from .models import *

Models = (AlertStatus, ProblemStatus, Unit, Control, BodyType,
          Application, Alert, Problem)

admin.site.register(Models)
