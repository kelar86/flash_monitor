# Generated by Django 2.1 on 2019-03-16 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rest_api', '0003_searchadvise'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='searchobject',
            name='application',
        ),
        migrations.RemoveField(
            model_name='searchobject',
            name='body_type',
        ),
        migrations.RemoveField(
            model_name='searchobject',
            name='control',
        ),
        migrations.RemoveField(
            model_name='searchobject',
            name='unit',
        ),
        migrations.RemoveField(
            model_name='searchresult',
            name='search_object',
        ),
        migrations.RemoveField(
            model_name='searchresult',
            name='user',
        ),
        migrations.DeleteModel(
            name='SearchObject',
        ),
        migrations.DeleteModel(
            name='SearchResult',
        ),
    ]
