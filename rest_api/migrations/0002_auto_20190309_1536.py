# Generated by Django 2.1 on 2019-03-09 15:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchobject',
            name='application',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.Application'),
        ),
        migrations.AlterField(
            model_name='searchobject',
            name='body_type',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.BodyType'),
        ),
        migrations.AlterField(
            model_name='searchobject',
            name='control',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.Control'),
        ),
        migrations.AlterField(
            model_name='searchobject',
            name='unit',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='monitor.Unit'),
        ),
    ]