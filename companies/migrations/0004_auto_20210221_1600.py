# Generated by Django 3.1.7 on 2021-02-21 14:00

import companies.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_auto_20210221_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='address',
            field=models.EmailField(max_length=254, unique=True, verbose_name='адрес электронной почты'),
        ),
        migrations.AlterField(
            model_name='phone',
            name='number',
            field=models.CharField(max_length=15, unique=True, validators=[companies.validators.PhoneValidator], verbose_name='номер'),
        ),
    ]