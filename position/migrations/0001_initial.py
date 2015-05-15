# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
        ('election_office_measure', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position_entered_id', models.BigIntegerField(null=True, blank=True)),
                ('date_entered', models.DateTimeField(null=True, verbose_name=b'date entered')),
                ('organization_id', models.BigIntegerField(null=True, blank=True)),
                ('politician_id', models.BigIntegerField(null=True, verbose_name=b'', blank=True)),
                ('stance', models.CharField(max_length=15, choices=[(b'SUPPORT_STRONG', b'Strong Supports'), (b'SUPPORT', b'Supports'), (b'UNDECIDED', b'Undecided on'), (b'NO_OPINION', b'No opinion'), (b'OPPOSE', b'Opposes'), (b'OPPOSE_STRONG', b'Strongly Opposes')])),
                ('statement_text', models.TextField(null=True, blank=True)),
                ('statement_html', models.TextField(null=True, blank=True)),
                ('more_info_url', models.URLField(null=True, verbose_name=b'url with more info about this position', blank=True)),
                ('candidate_campaign', models.ForeignKey(related_name='position_candidate', verbose_name=b'candidate campaign', blank=True, to='election_office_measure.CandidateCampaign', null=True)),
                ('measure_campaign', models.ForeignKey(related_name='position_measure', verbose_name=b'measure campaign', blank=True, to='election_office_measure.MeasureCampaign', null=True)),
            ],
            options={
                'ordering': ('date_entered',),
            },
        ),
        migrations.CreateModel(
            name='PositionEntered',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('position_id', models.BigIntegerField(null=True, blank=True)),
                ('organization_id', models.BigIntegerField(null=True, blank=True)),
                ('date_entered', models.DateTimeField(null=True, verbose_name=b'date entered')),
                ('tweet_source_id', models.BigIntegerField(null=True, blank=True)),
                ('candidate_campaign_id', models.BigIntegerField(null=True, verbose_name=b'id of candidate_campaign', blank=True)),
                ('politician_id', models.BigIntegerField(null=True, verbose_name=b'', blank=True)),
                ('measure_campaign_id', models.BigIntegerField(null=True, verbose_name=b'id of measure_campaign', blank=True)),
                ('stance', models.CharField(default=b'NO_OPINION', max_length=15, choices=[(b'SUPPORT_STRONG', b'Strong Supports'), (b'SUPPORT', b'Supports'), (b'UNDECIDED', b'Undecided on'), (b'NO_OPINION', b'No opinion'), (b'OPPOSE', b'Opposes'), (b'OPPOSE_STRONG', b'Strongly Opposes')])),
                ('statement_text', models.TextField(null=True, blank=True)),
                ('statement_html', models.TextField(null=True, blank=True)),
                ('more_info_url', models.URLField(null=True, verbose_name=b'url with more info about this position', blank=True)),
                ('from_scraper', models.BooleanField(default=False)),
                ('organization_certified', models.BooleanField(default=False)),
                ('volunteer_certified', models.BooleanField(default=False)),
                ('twitter_user_entered_position', models.ForeignKey(verbose_name=b'', to='twitter.TwitterUser', null=True)),
                ('voter_entering_position', models.ForeignKey(verbose_name=b'authenticated user who entered position', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('date_entered',),
            },
        ),
    ]
