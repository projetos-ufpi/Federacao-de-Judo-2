# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-20 00:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0012_faleconosco'),
    ]

    operations = [
        migrations.RenameField(
            model_name='academia',
            old_name='enredeco_academia',
            new_name='endereco_academia',
        ),
    ]