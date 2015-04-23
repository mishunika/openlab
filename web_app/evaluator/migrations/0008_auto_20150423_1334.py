# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0007_course_study_degree'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='course',
            unique_together=set([('study_degree', 'code')]),
        ),
    ]
