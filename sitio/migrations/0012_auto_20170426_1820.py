# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 21:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0011_auto_20170426_1817'),
    ]

    operations = [
        migrations.AlterField(
            model_name='astronauta',
            name='tipo',
            field=models.CharField(choices=[('apollo', 'Apollo'), ('gemini', 'Gemini'), ('mercury', 'Mercury')], default='apollo', max_length=9),
        ),
    ]
