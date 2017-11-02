# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 16:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('worldlink', '0006_profile_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.date.today, null=True, verbose_name='Date of Birth'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='static/images/profile-default.png', upload_to='worldlink/static/images', verbose_name='Profile Pic'),
        ),
    ]