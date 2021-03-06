# Generated by Django 2.1 on 2019-03-09 12:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monitor', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchObject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.Application')),
                ('body_type', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.BodyType')),
                ('control', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.Control')),
                ('unit', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.Unit')),
            ],
        ),
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
                ('search_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.SearchObject')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
