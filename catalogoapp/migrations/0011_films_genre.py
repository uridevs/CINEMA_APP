# Generated by Django 4.0.3 on 2022-04-05 22:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoapp', '0010_remove_films_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='films',
            name='genre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='catalogoapp.genre'),
        ),
    ]
