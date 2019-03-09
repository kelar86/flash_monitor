from django.db import models
from django.contrib.auth.models import User


class AlertCategory(models.Model):
    category_label = models.CharField(max_length=80)
    category = models.CharField(max_length=80, primary_key=True)


class AlertStatus(models.Model):
    status_label = models.CharField(max_length=80)
    status = models.CharField(max_length=80, primary_key=True)


class ProblemStatus(models.Model):
    status_label = models.CharField(max_length=80)
    status = models.CharField(max_length=80, primary_key=True)


class Unit(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(null=True)
    is_visiable = models.BooleanField(null=True)


class Control(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(null=True)
    is_visiable = models.BooleanField(null=True)


class BodyType(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(null=True)
    is_visiable = models.BooleanField(null=True)


class Application(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(null=True)
    has_controls = models.BooleanField(null=True)
    is_visiable = models.BooleanField(null=True)


class Alert(models.Model):
    alert_type = models.ForeignKey(
        AlertStatus, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()
    finish_date = models.DateField(null=True)
    category = models.ForeignKey(AlertCategory, on_delete=models.CASCADE)

    application = models.OneToOneField(Application, on_delete=models.CASCADE)

    control = models.ManyToManyField(Control, blank=True)
    unit = models.ManyToManyField(Unit, blank=True)
    body_type = models.ManyToManyField(BodyType, blank=True)

    description = models.TextField(null=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True)


class Problem(models.Model):
    status = models.ForeignKey(
        ProblemStatus, on_delete=models.SET_NULL, null=True)
    detection_date = models.DateTimeField()
    application = models.OneToOneField(Application, on_delete=models.CASCADE)
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, null=True)

    control = models.ManyToManyField(Control, blank=True)
    unit = models.ManyToManyField(Unit, blank=True)
    body_type = models.ManyToManyField(BodyType, blank=True)

    description = models.TextField(null=True)
    author = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
