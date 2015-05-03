# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0012_auto_20150429_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='ects',
            field=models.IntegerField(null=True),
        ),
    ]
