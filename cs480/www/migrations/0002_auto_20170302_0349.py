# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-02 03:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('www', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='image',
            field=models.CharField(max_length=200),
        ),
    ]
