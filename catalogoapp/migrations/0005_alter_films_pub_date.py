# Generated by Django 4.0.3 on 2022-04-05 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogoapp', '0004_rename_author_director'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='pub_date',
            field=models.DateField(verbose_name='date published'),
        ),
    ]