# Generated by Django 3.0.5 on 2020-05-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0007_auto_20200512_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about_me',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
