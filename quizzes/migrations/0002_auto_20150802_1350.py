# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quizzes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Taker Answer',
                'verbose_name_plural': 'Taker Answers',
            },
        ),
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice_text', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Question Answer',
                'verbose_name_plural': 'Question Answers',
            },
        ),
        migrations.RemoveField(
            model_name='questionchoice',
            name='question',
        ),
        migrations.RemoveField(
            model_name='takeranswer',
            name='question',
        ),
        migrations.RemoveField(
            model_name='takeranswer',
            name='taker',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='answer',
            new_name='answer_text',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='question',
            new_name='question_text',
        ),
        migrations.DeleteModel(
            name='QuestionChoice',
        ),
        migrations.DeleteModel(
            name='TakerAnswer',
        ),
        migrations.AddField(
            model_name='choice',
            name='question',
            field=models.ForeignKey(to='quizzes.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='question',
            field=models.ForeignKey(to='quizzes.Question'),
        ),
        migrations.AddField(
            model_name='answer',
            name='taker',
            field=models.ForeignKey(to='quizzes.Taker'),
        ),
    ]
