# Generated by Django 4.1.7 on 2023-04-19 09:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useractionsonimagesmodel',
            name='action_datetime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]