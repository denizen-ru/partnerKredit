# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 03:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0003_auto_20160522_0120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='offer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claim', to='claims.Offer'),
        ),
        migrations.AlterField(
            model_name='claim',
            name='questionnaire',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='claim', to='claims.Questionnaire'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='credit_organization',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='offer', to='accounts.CreditOrganization'),
        ),
        migrations.AlterField(
            model_name='questionnaire',
            name='partner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire', to='accounts.Partner'),
        ),
    ]