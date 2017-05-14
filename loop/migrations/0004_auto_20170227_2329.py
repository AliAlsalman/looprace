# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-28 07:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('loop', '0003_auto_20170227_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='address_city',
            field=models.CharField(max_length=50, verbose_name='City Name '),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_country',
            field=models.CharField(max_length=50, verbose_name='Country Name '),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_postal',
            field=models.CharField(blank=True, max_length=5, verbose_name='Postal Address (Optional) '),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_state',
            field=models.CharField(max_length=50, verbose_name='State / Province Name '),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_street',
            field=models.CharField(max_length=50, verbose_name='Street Name / Number '),
        ),
        migrations.AlterField(
            model_name='company',
            name='address_zip',
            field=models.CharField(blank=True, max_length=5, verbose_name='ZIP Code (Optional) '),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.FileField(null=True, upload_to='', verbose_name='Company Logo '),
        ),
        migrations.AlterField(
            model_name='company',
            name='email_address',
            field=models.EmailField(max_length=100, verbose_name='Email Address '),
        ),
        migrations.AlterField(
            model_name='company',
            name='founded_year',
            field=models.DateField(null=True, verbose_name='Year Founded '),
        ),
        migrations.AlterField(
            model_name='company',
            name='market_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Market Name '),
        ),
        migrations.AlterField(
            model_name='company',
            name='overview',
            field=models.TextField(null=True, verbose_name='Company Overview '),
        ),
        migrations.AlterField(
            model_name='company',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, verbose_name='Phone Number (Optional) '),
        ),
        migrations.AlterField(
            model_name='company',
            name='posted_date',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Posted Date'),
        ),
        migrations.AlterField(
            model_name='company',
            name='unique_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Registered Name '),
        ),
        migrations.AlterField(
            model_name='company',
            name='website_url',
            field=models.URLField(blank=True, verbose_name='Website URL (Optional) '),
        ),
        migrations.AlterField(
            model_name='contest',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Company', verbose_name='Company Name '),
        ),
        migrations.AlterField(
            model_name='contest',
            name='contest_ends',
            field=models.DateField(null=True, verbose_name='Contest Ends On '),
        ),
        migrations.AlterField(
            model_name='contest',
            name='contest_info',
            field=models.TextField(null=True, verbose_name='Contest Description '),
        ),
        migrations.AlterField(
            model_name='contest',
            name='contest_name',
            field=models.CharField(max_length=50, verbose_name='Contest Name '),
        ),
        migrations.AlterField(
            model_name='contest',
            name='contest_picture',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Contest Picture (Optional) '),
        ),
        migrations.AlterField(
            model_name='contest',
            name='posted_date',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Posted Date'),
        ),
        migrations.AlterField(
            model_name='contest',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Product', verbose_name='Product Name '),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Company', verbose_name='Company Name '),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_ends',
            field=models.DateField(null=True, verbose_name='Coupon Ends On '),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_info',
            field=models.TextField(null=True, verbose_name='Coupon Description '),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_name',
            field=models.CharField(max_length=50, verbose_name='Coupon Name '),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='coupon_picture',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Coupon Picture (Recommended) '),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='posted_date',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Posted Date'),
        ),
        migrations.AlterField(
            model_name='coupon',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Product', verbose_name='Product Name '),
        ),
        migrations.AlterField(
            model_name='offer',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Company', verbose_name='Company Name '),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_ends',
            field=models.DateField(null=True, verbose_name='Offer Ends On '),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_info',
            field=models.TextField(null=True, verbose_name='Offer Description '),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_name',
            field=models.CharField(max_length=50, verbose_name='Offer Name '),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_picture',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Offer Picture (Optional) '),
        ),
        migrations.AlterField(
            model_name='offer',
            name='offer_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, verbose_name='Offer Price (Optional) '),
        ),
        migrations.AlterField(
            model_name='offer',
            name='posted_date',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Posted Date'),
        ),
        migrations.AlterField(
            model_name='offer',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Product', verbose_name='Product Name '),
        ),
        migrations.AlterField(
            model_name='product',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loop.Company', verbose_name='Company Name '),
        ),
        migrations.AlterField(
            model_name='product',
            name='posted_date',
            field=models.DateField(auto_now_add=True, db_index=True, verbose_name='Posted Date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_madedate',
            field=models.DateField(blank=True, null=True, verbose_name='Product Made On (Optional) '),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=50, verbose_name='Product Name '),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_picture',
            field=models.FileField(blank=True, null=True, upload_to='', verbose_name='Product Picture (Optional) '),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_price',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Product Price '),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_type',
            field=models.CharField(blank=True, max_length=50, verbose_name='Product Type (Optional) '),
        ),
    ]
