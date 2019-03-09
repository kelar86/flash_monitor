# Generated by Django 2.1 on 2019-03-09 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('finish_date', models.DateField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='AlertCategory',
            fields=[
                ('category_label', models.CharField(max_length=80)),
                ('category', models.CharField(max_length=80, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='AlertStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_label', models.CharField(max_length=80)),
                ('status', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='')),
                ('has_controls', models.BooleanField()),
                ('is_visiable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='BodyType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='')),
                ('is_visiable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Control',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='')),
                ('is_visiable', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Problem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detection_date', models.DateTimeField()),
                ('description', models.TextField()),
                ('alert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.Alert')),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.Application')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('body_type', models.ManyToManyField(to='monitor.BodyType')),
                ('control', models.ManyToManyField(to='monitor.Control')),
            ],
        ),
        migrations.CreateModel(
            name='ProblemStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_label', models.CharField(max_length=80)),
                ('status', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='')),
                ('is_visiable', models.BooleanField()),
            ],
        ),
        migrations.AddField(
            model_name='problem',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitor.ProblemStatus'),
        ),
        migrations.AddField(
            model_name='problem',
            name='unit',
            field=models.ManyToManyField(to='monitor.Unit'),
        ),
        migrations.AddField(
            model_name='alert',
            name='alert_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='monitor.AlertStatus'),
        ),
        migrations.AddField(
            model_name='alert',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='alert',
            name='body_type',
            field=models.ManyToManyField(to='monitor.BodyType'),
        ),
        migrations.AddField(
            model_name='alert',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monitor.AlertCategory'),
        ),
        migrations.AddField(
            model_name='alert',
            name='control',
            field=models.ManyToManyField(to='monitor.Control'),
        ),
        migrations.AddField(
            model_name='alert',
            name='unit',
            field=models.ManyToManyField(to='monitor.Unit'),
        ),
    ]
