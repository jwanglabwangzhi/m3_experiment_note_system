# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-25 01:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0004_auto_20171024_2202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='summary',
            field=models.TextField(max_length=500),
        ),
    ]
