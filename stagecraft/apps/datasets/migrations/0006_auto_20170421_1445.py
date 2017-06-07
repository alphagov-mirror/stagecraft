# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 14:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('datasets', '0005_auto_20150707_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='owners',
            field=models.ManyToManyField(blank=True, related_name='data_sets', to='users.User'),
        ),
    ]
