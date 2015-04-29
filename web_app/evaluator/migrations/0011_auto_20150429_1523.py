# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0010_auto_20150424_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCase',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('file', models.FileField(storage=django.core.files.storage.FileSystemStorage(location='/app/evaluator_tests'), upload_to='')),
                ('lang', models.CharField(choices=[('P', 'Python'), ('R', 'Ruby')], max_length=1, default='B')),
                ('added', models.DateTimeField(auto_now_add=True)),
                ('assignment', models.ForeignKey(to='evaluator.Assignment')),
            ],
        ),
        migrations.AddField(
            model_name='submission',
            name='status',
            field=models.CharField(choices=[('N', 'New'), ('T', 'Testing'), ('P', 'Passed'), ('F', 'Failed')], max_length=1, default='B'),
        ),
    ]
