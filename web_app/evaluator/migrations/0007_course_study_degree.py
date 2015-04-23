# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0006_auto_20150423_1110'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='study_degree',
            field=models.CharField(max_length=1, default='B', choices=[('B', 'Bachelor'), ('M', 'Master')]),
        ),
    ]
