# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 20:30
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0007_auto_20170426_0307'),
    ]

    operations = [
        migrations.CreateModel(
            name='indicador',
            fields=[
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('percent', models.PositiveIntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(100)])),
            ],
            options={
                'verbose_name': 'Indicador',
                'verbose_name_plural': 'indicadores',
            },
        ),
    ]
