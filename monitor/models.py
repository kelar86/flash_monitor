from django.db import models
from django.contrib.auth.models import User


class AlertStatus(models.Model):
    status = models.CharField(max_length=255)


class ProblemStatus(models.Model):
    status = models.CharField(max_length=255)


class Unit(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    is_visiable = models.BooleanField()


class Control(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    is_visiable = models.BooleanField()


class BodyType(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    is_visiable = models.BooleanField()


class Application(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    has_controls = models.BooleanField()
    is_visiable = models.BooleanField()


class Alert(models.Model):
    alert_type = models.ForeignKey(
        AlertStatus, on_delete=models.SET_NULL, null=True)
    start_date = models.DateField()


class Problem(models.Model):
    status = models.ForeignKey(
        ProblemStatus, on_delete=models.SET_NULL, null=True)
    detection_date = models.DateTimeField()
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, null=True)

    control = models.ForeignKey(Control, on_delete=models.SET_NULL, null=True)
    unit = models.ForeignKey(Unit, on_delete=models.SET_NULL, null=True)
    body_type = models.ForeignKey(
        BodyType, on_delete=models.SET_NULL, null=True)

    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
