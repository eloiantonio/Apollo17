# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 22:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0012_auto_20170426_1820'),
    ]

    operations = [
        migrations.CreateModel(
            name='portfcl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descript', models.TextField(verbose_name='Nome & Descrição da Empresa')),
                ('logo', models.ImageField(upload_to='sitio/images/portifolio', verbose_name='Logo')),
                ('andament', models.CharField(choices=[('const', 'Em Construção'), ('lanc', 'Lançados')], default='const', max_length=1)),
            ],
            options={
                'verbose_name': 'Portifólio',
                'verbose_name_plural': 'Portifólio',
            },
        ),
        migrations.DeleteModel(
            name='apollo',
        ),
        migrations.DeleteModel(
            name='gemini',
        ),
        migrations.DeleteModel(
            name='mercury',
        ),
    ]
