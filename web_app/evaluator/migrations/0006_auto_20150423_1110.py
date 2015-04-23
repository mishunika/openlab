# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0005_auto_20150422_2004'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='title',
            new_name='title_en',
        ),
        migrations.AddField(
            model_name='course',
            name='title_ro',
            field=models.CharField(default='-', max_length=64),
            preserve_default=False,
        ),
    ]
