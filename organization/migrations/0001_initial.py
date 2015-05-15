# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=None, max_length=255, null=True, verbose_name=b'first name', blank=True)),
                ('url', models.URLField(null=True, verbose_name=b'url of the endorsing organization', blank=True)),
                ('twitter_handle', models.CharField(max_length=15, null=True, verbose_name=b'twitter handle')),
                ('organization_type', models.CharField(default=b'U', max_length=1, verbose_name=b'type of org', choices=[(b'3', b'Nonprofit 501c3'), (b'4', b'Nonprofit 501c4'), (b'P', b'Political Action Committee'), (b'C', b'Corporation'), (b'N', b'News Corporation'), (b'U', b'Unknown')])),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
