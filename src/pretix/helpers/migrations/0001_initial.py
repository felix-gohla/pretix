# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-20 07:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Thumbnail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=255)),
                ('size', models.CharField(max_length=255)),
                ('thumb', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='thumbnail',
            unique_together=set([('source', 'size')]),
        ),
    ]
