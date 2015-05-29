# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('position', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionListForCandidateCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.AddField(
            model_name='position',
            name='election_id',
            field=models.BigIntegerField(null=True, verbose_name=b'election id', blank=True),
        ),
        migrations.AddField(
            model_name='positionentered',
            name='election_id',
            field=models.BigIntegerField(null=True, verbose_name=b'election id', blank=True),
        ),
        migrations.AlterField(
            model_name='position',
            name='stance',
            field=models.CharField(max_length=15, choices=[(b'SUPPORT', b'Supports'), (b'STILL_DECIDING', b'Still deciding'), (b'NO_OPINION', b'No opinion'), (b'OPPOSE', b'Opposes')]),
        ),
        migrations.AlterField(
            model_name='positionentered',
            name='stance',
            field=models.CharField(default=b'NO_OPINION', max_length=15, choices=[(b'SUPPORT', b'Supports'), (b'STILL_DECIDING', b'Still deciding'), (b'NO_OPINION', b'No opinion'), (b'OPPOSE', b'Opposes')]),
        ),
    ]
