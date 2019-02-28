# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-04-05 16:14
from __future__ import unicode_literals

import articles.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_article_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.FileField(blank=True, upload_to='', validators=[articles.models.validate_file_extension], verbose_name='Image'),
        ),
    ]