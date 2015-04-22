# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0004_auto_20150422_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='professor',
            name='courses',
            field=models.ManyToManyField(blank=True, to='evaluator.Course'),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='enrolled_courses',
            field=models.ManyToManyField(blank=True, to='evaluator.Course'),
        ),
    ]
