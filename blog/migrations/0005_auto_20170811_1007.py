# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-11 10:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20170811_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='parent_comment',
            field=models.IntegerField(db_index=True, null=True),
        ),
    ]