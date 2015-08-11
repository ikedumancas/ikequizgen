# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question', models.TextField()),
                ('question_type', models.CharField(default=b'fb', max_length=2, choices=[(b'fb', b'Fill in the Blank'), (b'tf', b'True or False'), (b'mc', b'Multiple Choice')])),
                ('answer', models.TextField()),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='QuestionChoice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('choice', models.TextField()),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(to='quizzes.Question')),
            ],
            options={
                'verbose_name': 'Question Answer',
                'verbose_name_plural': 'Question Answers',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128)),
                ('title', models.CharField(max_length=200)),
                ('before_start_message', models.TextField(default=b'Select an answer for every question. Unanswered questions will be scored as incorrect.', null=True, blank=True)),
                ('after_end_message', models.TextField(default=b'Close this browser when you are done.', null=True, blank=True)),
                ('random_question_order', models.BooleanField(default=False)),
                ('show_result_after_submit', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Taker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('score', models.PositiveIntegerField(default=0)),
                ('quiz', models.ForeignKey(to='quizzes.Quiz')),
            ],
            options={
                'verbose_name': 'Taker',
                'verbose_name_plural': 'Takers',
            },
        ),
        migrations.CreateModel(
            name='TakerAnswer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('answer', models.TextField(null=True, blank=True)),
                ('question', models.ForeignKey(to='quizzes.Question')),
                ('taker', models.ForeignKey(to='quizzes.Taker')),
            ],
            options={
                'verbose_name': 'Taker Answer',
                'verbose_name_plural': 'Taker Answers',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(to='quizzes.Quiz'),
        ),
    ]
