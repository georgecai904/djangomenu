# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 08:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]