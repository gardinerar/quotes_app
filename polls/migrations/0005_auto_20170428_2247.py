# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-29 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_auto_20170428_2244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quotes',
            name='quotes_text',
        ),
        migrations.AddField(
            model_name='quotes',
            name='quote_text',
            field=models.CharField(default='gasp', max_length=200),
        ),
    ]
