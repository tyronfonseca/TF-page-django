# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-08-29 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_trabajos_abreviacion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trabajos',
            name='tipo',
            field=models.CharField(choices=[('app', 'APP'), ('web', 'WEB'), ('cus', 'CUSTOM')], max_length=3),
        ),
    ]
