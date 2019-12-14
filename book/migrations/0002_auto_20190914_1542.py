# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-14 15:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='libro',
            name='editor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='editor', to='book.Editorial'),
        ),
    ]
