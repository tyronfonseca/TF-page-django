# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-14 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20170813_2006'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habilidades',
            name='tipo',
        ),
        migrations.AlterField(
            model_name='habilidades',
            name='imagen',
            field=models.ImageField(upload_to='images/habilidades'),
        ),
    ]
