from django.db import models
from django.contrib.auth.models import User


class AlertCategory(models.Model):
    category_label = models.CharField(max_length=80)
    category = models.CharField(max_length=80, primary_key=True)

    def __str__(self):
        return self.category_label


class AlertStatus(models.Model):
    status_label = models.CharField(max_length=80)
    status = models.CharField(max_length=80, primary_key=True)

    def __str__(self):
        return self.status_label


class ProblemStatus(models.Model):
    status_label = models.CharField(max_length=80)
    status = models.CharField(max_length=80, primary_key=True)

    def __str__(self):
        return self.status_label


class Unit(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(null=True, blank=True)
    is_visiable = models.BooleanField(default=True)
    search_fields = ('name',)

    def __str__(self):
        return self.name


class ControlType(models.Model):
    name = models.CharField(max_length=80)
    icon = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Control(models.Model):
    name = models.CharField(max_length=255)
    is_visiable = models.BooleanField(default=True)
    control_type = models.ForeignKey(ControlType, on_delete=models.CASCADE)
    search_fields = ('name',)

    def __str__(self):
        return self.name


class BodyType(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(null=True, blank=True)
    is_visiable = models.BooleanField(default=True)
    search_fields = ('name',)

    def __str__(self):
        return self.name


class Application(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(null=True, blank=True)
    has_controls = models.BooleanField(default=False)
    is_visiable = models.BooleanField(default=True)
    search_fields = ('name',)

    def __str__(self):
        return self.name


class Alert(models.Model):
    alert_type = models.ForeignKey(
        AlertStatus, on_delete=models.CASCADE)
    start_date = models.DateField()
    finish_date = models.DateField(null=True, blank=True)
    category = models.ForeignKey(AlertCategory, on_delete=models.CASCADE)

    application = models.ForeignKey(Application, on_delete=models.CASCADE)

    control = models.ManyToManyField(Control, blank=True, null=True)
    unit = models.ManyToManyField(Unit, blank=True, null=True)
    body_type = models.ManyToManyField(BodyType, blank=True, null=True)

    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s %s' % (self.start_date, self.application)


class Problem(models.Model):
    status = models.ForeignKey(
        ProblemStatus, on_delete=models.SET_NULL, null=True)
    detection_date = models.DateTimeField()
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE)
    alert = models.ForeignKey(
        Alert, on_delete=models.CASCADE, null=True, blank=True)

    control = models.ManyToManyField(Control, blank=True, null=True)
    unit = models.ManyToManyField(Unit, blank=True, null=True)
    body_type = models.ManyToManyField(BodyType, blank=True, null=True)

    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '%s %s' % (self.detection_date, self.application)
