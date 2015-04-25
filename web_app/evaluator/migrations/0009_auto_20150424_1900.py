# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0008_auto_20150423_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentgroup',
            name='number',
            field=models.PositiveSmallIntegerField(default=111),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='studentgroup',
            name='speciality',
            field=models.CharField(default='-', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='name',
            field=models.CharField(max_length=4),
        ),
    ]
