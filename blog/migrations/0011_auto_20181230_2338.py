# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-12-30 23:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20181230_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_detail',
            name='time_now',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 12, 30, 23, 38, 3, 307770, tzinfo=utc)),
        ),
    ]
