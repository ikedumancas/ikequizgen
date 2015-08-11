# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0002_auto_20150802_1350'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={},
        ),
        migrations.AlterModelOptions(
            name='taker',
            options={},
        ),
        migrations.RemoveField(
            model_name='question',
            name='password',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='random_question_order',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='show_result_after_submit',
        ),
        migrations.AddField(
            model_name='quiz',
            name='show_answers',
            field=models.BooleanField(default=False, verbose_name=b"show taker's answers and evaluation after quiz"),
        ),
        migrations.AddField(
            model_name='quiz',
            name='show_score',
            field=models.BooleanField(default=False, verbose_name=b"show taker's score quiz"),
        ),
    ]
