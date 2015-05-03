# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0011_auto_20150429_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('T', 'Testing'), ('P', 'Passed'), ('F', 'Failed')], default='N', max_length=1),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='lang',
            field=models.CharField(choices=[('P', 'Python'), ('R', 'Ruby')], default='P', max_length=1),
        ),
    ]
