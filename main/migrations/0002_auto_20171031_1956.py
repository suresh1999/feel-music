# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-31 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='updated_on',
            field=models.DateTimeField(auto_created=True),
        ),
    ]