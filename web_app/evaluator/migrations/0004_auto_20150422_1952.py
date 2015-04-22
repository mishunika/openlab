# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('evaluator', '0003_auto_20150422_0008'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('assignment', models.ForeignKey(to='evaluator.Assignment')),
            ],
        ),
        migrations.AlterField(
            model_name='professor',
            name='courses',
            field=models.ManyToManyField(blank=True, to='evaluator.Course', null=True),
        ),
        migrations.AlterField(
            model_name='studentgroup',
            name='enrolled_courses',
            field=models.ManyToManyField(blank=True, to='evaluator.Course', null=True),
        ),
        migrations.AddField(
            model_name='feed',
            name='professor',
            field=models.ForeignKey(to='evaluator.Professor'),
        ),
    ]
