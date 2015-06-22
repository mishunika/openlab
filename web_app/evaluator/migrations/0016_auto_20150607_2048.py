# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0015_auto_20150607_2037'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentgroup',
            name='enrolled_courses',
        ),
        migrations.DeleteModel(
            name='StudentGroup',
        ),
    ]
