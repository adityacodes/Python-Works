# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-09 04:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='tags',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
