# Generated by Django 4.0.3 on 2022-04-05 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoapp', '0008_alter_films_genre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='genre',
            name='last_name',
        ),
    ]
