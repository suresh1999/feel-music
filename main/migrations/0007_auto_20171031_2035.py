# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20171031_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='download_link',
            field=models.URLField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='song',
            name='video_link',
            field=models.URLField(default=' '),
            preserve_default=False,
        ),
    ]