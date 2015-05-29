# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FollowOrganization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voter_id', models.BigIntegerField(null=True, blank=True)),
                ('organization_id', models.BigIntegerField(null=True, blank=True)),
                ('following_status', models.CharField(default=b'FOLLOW', max_length=15, choices=[(b'FOLLOW', b'Following'), (b'STOP_FOLLOWING', b'Not Following'), (b'FOLLOW_IGNORE', b'Ignoring')])),
                ('date_last_changed', models.DateTimeField(null=True, verbose_name=b'date last changed')),
            ],
        ),
        migrations.CreateModel(
            name='FollowOrganizationManager',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
    ]
