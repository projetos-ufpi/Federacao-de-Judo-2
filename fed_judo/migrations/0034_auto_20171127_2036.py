# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-27 22:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0033_auto_20171127_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fed_judo.TipoUsuario'),
        ),
    ]
