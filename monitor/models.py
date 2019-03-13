from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.timezone import now


class AlertCategory(models.Model):
    category_label = models.CharField(max_length=80)
    category = models.CharField(max_length=80, primary_key=True)

    def __str__(self):
        return self.category_label

    class Meta:
        verbose_name = u"Категория алерта"
        verbose_name_plural = u"Категории алертов"


class AlertStatus(models.Model):
    status_label = models.CharField(max_length=80)
    status = models.CharField(max_length=80, primary_key=True)

    def __str__(self):
        return self.status_label

    class Meta:
        verbose_name = u"Статус алерта"
        verbose_name_plural = u"Статусы алертов"


class ProblemStatus(models.Model):
    status_label = models.CharField(max_length=80)
    status = models.CharField(max_length=80, primary_key=True)

    def __str__(self):
        return self.status_label

    class Meta:
        verbose_name = u"Статус проблемы"
        verbose_name_plural = u"Статусы проблем"


class Unit(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Название")
    icon = models.ImageField(null=True, blank=True, verbose_name=u"Иконка")
    is_visiable = models.BooleanField(default=True, verbose_name=u"Отображать для клиента")
    search_fields = ("name",)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Агрегат"
        verbose_name_plural = u"Агрегаты"


class Control(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Название")
    is_visiable = models.BooleanField(default=True, verbose_name=u"Отображать для клиента")
    icon = models.ImageField(null=True, blank=True, verbose_name=u"Иконка")
    search_fields = ("name",)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Блок управления"
        verbose_name_plural = u"Блоки управления"


class BodyType(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Название")
    icon = models.ImageField(null=True, blank=True, verbose_name=u"Иконка")
    is_visiable = models.BooleanField(default=True, verbose_name=u"Отображать для клиента")
    search_fields = ("name",)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Тип кузова"
        verbose_name_plural = u"Типы кузова"


class Application(models.Model):
    name = models.CharField(max_length=255, verbose_name=u"Название")
    icon = models.ImageField(null=True, blank=True, verbose_name=u"Иконка")
    has_controls = models.BooleanField(default=False, verbose_name=u"Наличие блоков управления")
    is_visiable = models.BooleanField(default=True, verbose_name=u"Отображать для клиента")
    search_fields = ("name",)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = u"Приложение"
        verbose_name_plural = u"Приложения"


class Alert(models.Model):
    alert_type = models.ForeignKey(
        AlertStatus, on_delete=models.CASCADE, default="ACTIVE", verbose_name=u"Статус")
    start_date = models.DateField(default=now, verbose_name=u"Дата начала")
    finish_date = models.DateField(null=True, blank=True, verbose_name=u"Дата окончания(план)")
    category = models.ForeignKey(AlertCategory, on_delete=models.CASCADE, verbose_name=u"Категория алерта")

    application = models.ForeignKey(Application, on_delete=models.CASCADE, verbose_name=u"Приложение")

    control = models.ManyToManyField(Control, blank=True, null=True, verbose_name=u"Блоки управления")
    unit = models.ManyToManyField(Unit, blank=True, null=True, verbose_name=u"Агрегаты")
    body_type = models.ManyToManyField(BodyType, blank=True, null=True, verbose_name=u"Типы кузова")

    description = models.TextField(blank=True, verbose_name=u"Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name=u"Автор")

    @property
    def is_planed(self):
        return self.start_date > now.date()

    def __str__(self):
        return "%s %s" % (self.start_date, self.application)

    class Meta:
        verbose_name = u"Алерт"
        verbose_name_plural = u"Алерты"


class Problem(models.Model):
    status = models.ForeignKey(
        ProblemStatus, on_delete=models.SET_NULL, null=True, default="NEW", verbose_name=u"Статус")
    detection_date = models.DateTimeField(default=now, verbose_name=u"Дата и время обнаружения")
    application = models.ForeignKey(
        Application, on_delete=models.CASCADE, verbose_name=u"Приложение")
    alert = models.ForeignKey(
        Alert, on_delete=models.CASCADE, null=True, blank=True, verbose_name=u"Алерт")

    control = models.ManyToManyField(Control, blank=True, null=True, verbose_name=u"Блоки управления")
    unit = models.ManyToManyField(Unit, blank=True, null=True, verbose_name=u"Агрегаты")
    body_type = models.ManyToManyField(BodyType, blank=True, null=True, verbose_name=u"Типы кузова")

    description = models.TextField(blank=True, verbose_name=u"Описание")
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, verbose_name=u"Автор")

    def __str__(self):
        return "%s %s" % (self.detection_date, self.application)

    class Meta:
        verbose_name = u"Проблема"
        verbose_name_plural = u"Проблемы"
