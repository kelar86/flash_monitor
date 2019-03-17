# Generated by Django 2.1 on 2019-03-16 09:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0008_auto_20190316_0524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='finish_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Дата окончания(план)'),
        ),
        migrations.AlterField(
            model_name='alert',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 16, 9, 10, 4, 369499), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='detection_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 16, 9, 10, 4, 373090), verbose_name='Дата и время обнаружения'),
        ),
    ]
