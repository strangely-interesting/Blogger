# Generated by Django 3.0.5 on 2020-05-21 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0009_profile_last_visited'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='last_visited',
            field=models.DateTimeField(),
        ),
    ]
