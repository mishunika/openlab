# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='professors',
        ),
        migrations.RemoveField(
            model_name='course',
            name='students',
        ),
        migrations.AddField(
            model_name='professor',
            name='courses',
            field=models.ManyToManyField(blank=True, to='evaluator.Course'),
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='evaluator.Course'),
        ),
    ]
