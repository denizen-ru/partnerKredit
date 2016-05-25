# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 09:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CreditOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='creditorganization', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Credit Organizations',
                'verbose_name': 'Credit Organization',
            },
        ),
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='partner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Partners',
                'verbose_name': 'Partner',
            },
        ),
        migrations.CreateModel(
            name='SuperUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='superuser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Super Users',
                'verbose_name': 'Super User',
            },
        ),
    ]
