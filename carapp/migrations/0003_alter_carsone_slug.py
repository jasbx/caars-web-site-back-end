# Generated by Django 5.0.1 on 2024-05-07 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_carsone_slug_carstwo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carsone',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]
