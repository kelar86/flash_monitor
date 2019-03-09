from monitor.models import *
from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class SearchObject(models.Model):

    application = models.OneToOneField(
        Application, null=True, on_delete=models.CASCADE)

    control = models.OneToOneField(
        Control, null=True, on_delete=models.CASCADE)

    unit = models.OneToOneField(
        Unit, null=True, on_delete=models.CASCADE)

    body_type = models.OneToOneField(
        BodyType, null=True, on_delete=models.CASCADE)


class SearchResult(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    date = models.DateTimeField(default=now, editable=False)
    search_object = models.ForeignKey(SearchObject, on_delete=models.CASCADE)
