# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-11 12:01
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20170811_1007'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='user_id',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='body',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='thumb',
            field=models.ImageField(storage=django.core.files.storage.FileSystemStorage(location='/mnt/d/code/blogs/thumbs/photos'), upload_to=''),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.CharField(default='', max_length=256),
        ),
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=''),
        ),
    ]