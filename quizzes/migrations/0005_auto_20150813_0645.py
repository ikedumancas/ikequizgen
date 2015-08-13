# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0004_auto_20150811_1354'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='choice',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'ordering': ['-timestamp'], 'verbose_name': 'Quiz', 'verbose_name_plural': 'Quizzes'},
        ),
        migrations.AddField(
            model_name='choice',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='order',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name=b'active'),
        ),
    ]
