# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 14:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20170702_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='likesperday',
            name='fb_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likesperday', to='api.PagesModel'),
        ),
        migrations.AlterField(
            model_name='postsmodel',
            name='fb_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='api.PagesModel'),
        ),
    ]
