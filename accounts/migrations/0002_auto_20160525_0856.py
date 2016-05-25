# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 05:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditorganization',
            name='creditorganization_title',
            field=models.CharField(default='title', max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='partner',
            name='partner_title',
            field=models.CharField(default='title', max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='superuser',
            name='superuser_title',
            field=models.CharField(default='title', max_length=255, verbose_name='Title'),
            preserve_default=False,
        ),
    ]
