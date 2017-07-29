# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-29 22:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afip', '0028_taxpayer__copy_active_since'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taxpayerprofile',
            name='active_since',
        ),
        migrations.AlterField(
            model_name='taxpayer',
            name='active_since',
            field=models.DateField(help_text='Date since which this taxpayer has been legally active.', verbose_name='active since'),
        ),
    ]
