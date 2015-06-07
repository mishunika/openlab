# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0014_submission_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='group',
        ),
        migrations.AddField(
            model_name='student',
            name='courses',
            field=models.ManyToManyField(blank=True, to='evaluator.Course'),
        ),
    ]
