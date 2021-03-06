# Generated by Django 3.1.7 on 2021-02-21 13:37

import companies.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_auto_20210221_1408'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=150, verbose_name='владелец')),
                ('address', models.EmailField(max_length=254, verbose_name='адрес электронной почты')),
            ],
            options={
                'verbose_name': 'email',
                'verbose_name_plural': 'emails',
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner', models.CharField(max_length=150, verbose_name='владелец')),
                ('number', models.CharField(max_length=15, validators=[companies.validators.PhoneValidator], verbose_name='номер')),
            ],
            options={
                'verbose_name': 'телефон',
                'verbose_name_plural': 'телефоны',
            },
        ),
        migrations.AddField(
            model_name='company',
            name='emails',
            field=models.ManyToManyField(to='companies.Email', verbose_name='emails'),
        ),
        migrations.AddField(
            model_name='company',
            name='phones',
            field=models.ManyToManyField(to='companies.Phone', verbose_name='phones'),
        ),
    ]
