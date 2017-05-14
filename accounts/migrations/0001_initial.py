# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 07:49
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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.FileField(null=True, upload_to='', verbose_name='Profile picture ')),
                ('phone_number', models.IntegerField(verbose_name='Phone Number (Optional) ')),
                ('website_url', models.URLField(blank=True, verbose_name='Website URL (Optional) ')),
                ('address_country', models.CharField(max_length=50, verbose_name='Country Name ')),
                ('address_state', models.CharField(max_length=50, verbose_name='State / Province Name ')),
                ('address_city', models.CharField(max_length=50, verbose_name='City Name ')),
                ('address_zip', models.CharField(blank=True, max_length=5, verbose_name='ZIP Code (Optional) ')),
                ('address_street', models.CharField(max_length=50, verbose_name='Street Name / Number (Optional) ')),
                ('address_postal', models.CharField(blank=True, max_length=5, verbose_name='Postal Address (Optional) ')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
