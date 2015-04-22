# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0002_auto_20150417_2131'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('enrolled_courses', models.ManyToManyField(to='evaluator.Course', blank=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='courses',
        ),
        migrations.AddField(
            model_name='student',
            name='group',
            field=models.ForeignKey(to='evaluator.StudentGroup', blank=True, null=True),
        ),
    ]
