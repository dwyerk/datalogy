# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-08 00:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('challenges', '0003_challenge_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='challenge',
            name='slug',
            field=models.SlugField(default=''),
            preserve_default=False,
        ),
    ]