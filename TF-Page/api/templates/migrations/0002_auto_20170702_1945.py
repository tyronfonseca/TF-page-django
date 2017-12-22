# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-02 19:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikesPerDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('number_likes', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PagesModel',
            fields=[
                ('fb_id', models.IntegerField(db_index=True, primary_key=True, serialize=False, unique=True)),
                ('likes', models.IntegerField()),
                ('name', models.CharField(max_length=124)),
            ],
        ),
        migrations.CreateModel(
            name='PostsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_id', models.IntegerField()),
                ('post_type', models.CharField(max_length=30)),
                ('reactions', models.TextField()),
                ('comments', models.TextField()),
                ('fb_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PagesModel')),
            ],
        ),
        migrations.AddField(
            model_name='likesperday',
            name='fb_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.PagesModel'),
        ),
    ]
