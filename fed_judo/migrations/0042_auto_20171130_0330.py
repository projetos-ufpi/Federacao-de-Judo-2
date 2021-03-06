# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-30 05:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fed_judo', '0041_noticia_descricao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='eventos_cadastrado',
        ),
        migrations.AddField(
            model_name='usuario',
            name='eventos_cadastrado',
            field=models.ManyToManyField(to='fed_judo.Evento'),
        ),
        migrations.RemoveField(
            model_name='usuario',
            name='tipo_usuario',
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario',
            field=models.ManyToManyField(default=1, to='fed_judo.TipoUsuario'),
        ),
    ]
