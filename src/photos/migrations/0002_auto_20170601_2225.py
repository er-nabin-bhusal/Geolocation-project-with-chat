# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-01 16:40
from __future__ import unicode_literals

from django.db import migrations, models
import photos.models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture',
            name='photo',
            field=models.ImageField(null=True, upload_to=photos.models.upload_location),
        ),
    ]
