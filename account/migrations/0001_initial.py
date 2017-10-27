# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-22 09:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('name', models.CharField(default='null', max_length=50)),
                ('student_id', models.CharField(default='null', max_length=9)),
                ('email', models.EmailField(default='null', max_length=254, unique=True)),
                ('password', models.CharField(default='null', max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
