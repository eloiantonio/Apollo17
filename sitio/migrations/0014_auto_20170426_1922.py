# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0013_auto_20170426_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='portfcl',
            name='andament',
            field=models.CharField(choices=[('const', 'Em Construção'), ('portfl', 'Lançados')], default='const', max_length=9),
        ),
    ]