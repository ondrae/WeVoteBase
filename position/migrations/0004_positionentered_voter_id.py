# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0003_auto_20150517_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionentered',
            name='voter_id',
            field=models.BigIntegerField(null=True, blank=True),
        ),
    ]
