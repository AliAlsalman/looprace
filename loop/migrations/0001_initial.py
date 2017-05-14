# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-16 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('market_name', models.CharField(max_length=50, unique=True)),
                ('unique_name', models.CharField(max_length=100, unique=True)),
                ('overview', models.TextField()),
                ('founded_year', models.DateField()),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('email_address', models.EmailField(max_length=100)),
                ('website_url', models.URLField()),
                ('logo', models.ImageField(max_length=500, upload_to='')),
                ('address_country', models.CharField(max_length=50)),
                ('address_state', models.CharField(max_length=50)),
                ('address_city', models.CharField(max_length=50)),
                ('address_zip', models.IntegerField()),
                ('address_street', models.CharField(max_length=50)),
                ('address_postal', models.IntegerField()),
                ('posted_date', models.DateField(auto_now_add=True, db_index=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_name', models.CharField(max_length=50)),
                ('contest_description', models.TextField()),
                ('contest_value', models.CharField(max_length=50)),
                ('contest_duration', models.DateField(auto_now_add=True, db_index=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Company', verbose_name='the related company')),
            ],
        ),
        migrations.CreateModel(
            name='Coupon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coupon_name', models.CharField(max_length=50)),
                ('coupon_description', models.TextField()),
                ('coupon_validity', models.DateField(auto_now_add=True, db_index=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Company', verbose_name='the related company')),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(max_length=50)),
                ('offer_duration', models.CharField(max_length=50)),
                ('offer_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('offer_date', models.DateField(auto_now_add=True, db_index=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Company', verbose_name='the related company')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50)),
                ('product_type', models.CharField(max_length=50)),
                ('product_price', models.DecimalField(decimal_places=3, max_digits=10)),
                ('product_date', models.DateField(auto_now_add=True, db_index=True)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Company', verbose_name='the related company')),
            ],
        ),
        migrations.AddField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Product', verbose_name='the related product'),
        ),
        migrations.AddField(
            model_name='coupon',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Product', verbose_name='the related product'),
        ),
        migrations.AddField(
            model_name='contest',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Product', verbose_name='the related product'),
        ),
    ]