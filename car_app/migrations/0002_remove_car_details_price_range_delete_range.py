# Generated by Django 5.0.6 on 2024-06-28 10:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='car_details',
            name='price_range',
        ),
        migrations.DeleteModel(
            name='Range',
        ),
    ]