# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-27 17:11
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0022_auto_20170427_1335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='astronauta',
            name='text',
        ),
        migrations.AddField(
            model_name='astronauta',
            name='texto',
            field=ckeditor.fields.RichTextField(default='Texto'),
            preserve_default=False,
        ),
    ]
