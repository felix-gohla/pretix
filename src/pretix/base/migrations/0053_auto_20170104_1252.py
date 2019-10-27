# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-04 12:52
from __future__ import unicode_literals

import django.core.validators
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import pretix.base.validators


class Migration(migrations.Migration):

    dependencies = [
        ('pretixbase', '0052_auto_20161231_1533'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequiredAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('done', models.BooleanField(default=False)),
                ('action_type', models.CharField(max_length=255)),
                ('data', models.TextField(default='{}')),
            ],
            options={
                'ordering': ('datetime',),
            },
        ),
        migrations.AlterField(
            model_name='event',
            name='slug',
            field=models.SlugField(help_text='Should be short, only contain lowercase letters and numbers, and must be unique among your events. This will be used in order codes, invoice numbers, links and bank transfer references.', validators=[django.core.validators.RegexValidator(message='The slug may only contain letters, numbers, dots and dashes.', regex='^[a-zA-Z0-9.-]+$'), pretix.base.validators.EventSlugBanlistValidator()], verbose_name='Short form'),
        ),
        migrations.AddField(
            model_name='requiredaction',
            name='event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pretixbase.Event'),
        ),
        migrations.AddField(
            model_name='requiredaction',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]
