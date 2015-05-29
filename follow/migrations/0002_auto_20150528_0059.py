# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('follow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FollowOrganizationList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AlterField(
            model_name='followorganization',
            name='following_status',
            field=models.CharField(default=b'FOLLOWING', max_length=15, choices=[(b'FOLLOWING', b'Following'), (b'STOP_FOLLOWING', b'Not Following'), (b'FOLLOW_IGNORE', b'Ignoring')]),
        ),
    ]
