# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0009_auto_20150424_1900'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentgroup',
            name='speciality',
            field=models.CharField(max_length=255),
        ),
    ]
