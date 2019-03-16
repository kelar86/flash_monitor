from monitor.models import *
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.db.models.signals import post_save


class SearchAdvise(models.Model):
    schema = models.TextField()


from .signals import *
