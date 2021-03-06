# Generated by Django 2.1 on 2019-03-24 15:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0009_auto_20190316_0910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 15, 5, 49, 841838), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='detection_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 24, 15, 5, 49, 845497), verbose_name='Дата и время обнаружения'),
        ),
    ]
