# Generated by Django 3.1.7 on 2021-02-21 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='название')),
                ('contact_person', models.CharField(max_length=150, verbose_name='контактное лицо')),
                ('description', models.TextField(verbose_name='описание')),
                ('address', models.CharField(max_length=200, verbose_name='адрес')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='дата создания записи')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='дата изменения записи')),
            ],
            options={
                'verbose_name': 'компания',
                'verbose_name_plural': 'компании',
            },
        ),
    ]
