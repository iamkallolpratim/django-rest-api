# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-08 11:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quickstart', '0002_auto_20160808_1101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='pub_date',
            new_name='published_date',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question_text',
            new_name='question',
        ),
    ]
