# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0013_course_ects'),
    ]

    operations = [
        migrations.AddField(
            model_name='submission',
            name='file',
            field=models.FileField(null=True, storage=django.core.files.storage.FileSystemStorage(location='/app/evaluator_submissions'), upload_to=''),
        ),
    ]
