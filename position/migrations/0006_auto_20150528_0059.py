# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0005_positionenteredmanager'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='stance',
            field=models.CharField(max_length=15, choices=[(b'SUPPORT', b'Supports'), (b'STILL_DECIDING', b'Still deciding'), (b'NO_STANCE', b'No stance'), (b'INFO_ONLY', b'Information only'), (b'OPPOSE', b'Opposes')]),
        ),
        migrations.AlterField(
            model_name='positionentered',
            name='stance',
            field=models.CharField(default=b'NO_STANCE', max_length=15, choices=[(b'SUPPORT', b'Supports'), (b'STILL_DECIDING', b'Still deciding'), (b'NO_STANCE', b'No stance'), (b'INFO_ONLY', b'Information only'), (b'OPPOSE', b'Opposes')]),
        ),
    ]
