# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 14:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_task', '0007_auto_20170610_0006'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='likers',
            field=models.ManyToManyField(blank=True, related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
    ]
