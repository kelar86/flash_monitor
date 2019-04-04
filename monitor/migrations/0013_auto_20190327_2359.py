# Generated by Django 2.1 on 2019-03-27 23:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0012_auto_20190327_2254'),
    ]

    operations = [
        migrations.RenameField(
            model_name='controltype',
            old_name='image',
            new_name='icon',
        ),
        migrations.AlterField(
            model_name='alert',
            name='start_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 23, 59, 51, 531188), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='problem',
            name='detection_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 27, 23, 59, 51, 534782), verbose_name='Дата и время обнаружения'),
        ),
    ]