# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-07 07:05
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20170407_0004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadvideo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
