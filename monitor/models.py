from django.db import models
from django.contrib.auth.models import User


class AlertCategory(models.Model):
    category_label = models.CharField(max_length=80)
    category = models.CharField(max_length=80, primary_key=True)


class AlertStatus(models.Model):
    status_label = models.CharField(max_length=80)
    status = models.CharField(max_length=80)


class ProblemStatus(models.Model):
    status_label = models.CharField(max_length=80)
    status = models.CharField(max_length=80)


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
    finish_date = models.DateField()
    category = models.ForeignKey(AlertCategory, on_delete=models.CASCADE)

    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    control = models.ManyToManyField(Control)
    unit = models.ManyToManyField(Unit)
    body_type = models.ManyToManyField(BodyType)

    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)


class Problem(models.Model):
    status = models.ForeignKey(
        ProblemStatus, on_delete=models.SET_NULL, null=True)
    detection_date = models.DateTimeField()
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    alert = models.ForeignKey(Alert, on_delete=models.CASCADE, null=True)

    control = models.ManyToManyField(Control)
    unit = models.ManyToManyField(Unit)
    body_type = models.ManyToManyField(BodyType)

    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
