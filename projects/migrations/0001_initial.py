# Generated by Django 3.1.7 on 2021-03-12 12:54

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('companies', '0007_auto_20210224_1458'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='название')),
                ('description', tinymce.models.HTMLField(verbose_name='описание')),
                ('start_date', models.DateField(verbose_name='начало')),
                ('end_date', models.DateField(verbose_name='окончание')),
                ('price', models.DecimalField(decimal_places=2, max_digits=20, verbose_name='цена')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='companies.company', verbose_name='компания')),
            ],
            options={
                'verbose_name': 'проект',
                'verbose_name_plural': 'проекты',
            },
        ),
    ]
