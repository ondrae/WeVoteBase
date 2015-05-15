# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hashtag_text', models.CharField(max_length=255, null=True, verbose_name=b'the text for a single hashtag', blank=True)),
                ('twitter_handle', models.CharField(max_length=15, null=True, verbose_name=b'twitter handle that we want to link to something', blank=True)),
                ('keywords', models.CharField(max_length=255, null=True, verbose_name=b'text that might be found in a tweet', blank=True)),
            ],
        ),
    ]
