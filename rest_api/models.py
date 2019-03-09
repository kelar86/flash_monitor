from django.db import models
from django.contrib.auth.models import User
from monitor.models import *


class QueryResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    application_result = models.ForeignKey(
        Application, on_delete=models.SET_NULL, null=True)
