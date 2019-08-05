# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2019-07-20 17:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_items'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='details', to=settings.AUTH_USER_MODEL),
        ),
    ]
