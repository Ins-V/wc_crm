# Generated by Django 3.1.7 on 2021-03-15 13:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interactions', '0002_auto_20210314_1238'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='interaction',
            name='company',
        ),
    ]