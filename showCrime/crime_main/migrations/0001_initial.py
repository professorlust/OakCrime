# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-31 22:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='OakCrime',
            fields=[
                ('idx', models.IntegerField(primary_key=True, serialize=False)),
                ('opd_rd', models.CharField(max_length=10)),
                ('oidx', models.IntegerField()),
                ('cdate', models.DateField()),
                ('ctime', models.TimeField()),
                ('ctype', models.CharField(blank=True, max_length=50, null=True)),
                ('desc', models.CharField(blank=True, max_length=200, null=True)),
                ('beat', models.CharField(blank=True, max_length=20, null=True)),
                ('addr', models.CharField(blank=True, max_length=100, null=True)),
                ('lat', models.FloatField(null=True)),
                ('long', models.FloatField(null=True)),
                ('ucr', models.CharField(blank=True, max_length=5, null=True)),
                ('statute', models.CharField(blank=True, max_length=50, null=True)),
                ('crimeCat', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
