# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BallotItemCache',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('voter_id', models.IntegerField(default=1, verbose_name=b'the voter unique id')),
                ('election_id', models.CharField(max_length=20, null=True, verbose_name=b'election id')),
                ('google_civic_election_id', models.CharField(max_length=20, null=True, verbose_name=b'google civic election id')),
                ('contest_office_id', models.CharField(max_length=254, null=True, verbose_name=b'contest_office_id id', blank=True)),
                ('contest_measure_id', models.CharField(max_length=254, null=True, verbose_name=b'contest_measure unique id', blank=True)),
                ('ballot_order', models.SmallIntegerField(null=True, verbose_name=b'the order this item should appear on the ballot', blank=True)),
                ('ballot_item_label', models.CharField(max_length=254, null=True, verbose_name=b'a label we can sort by', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CandidateCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('election_id', models.IntegerField(null=True, verbose_name=b'election unique identifier', blank=True)),
                ('contest_office_id', models.CharField(max_length=254, null=True, verbose_name=b'contest_office_id id', blank=True)),
                ('politician_id', models.IntegerField(null=True, verbose_name=b'politician unique identifier', blank=True)),
                ('candidate_name', models.CharField(max_length=254, verbose_name=b'candidate name')),
                ('party', models.CharField(max_length=254, null=True, verbose_name=b'party', blank=True)),
                ('photo_url', models.CharField(max_length=254, null=True, verbose_name=b'photoUrl', blank=True)),
                ('order_on_ballot', models.CharField(max_length=254, null=True, verbose_name=b'order on ballot', blank=True)),
                ('google_civic_election_id', models.CharField(max_length=254, null=True, verbose_name=b'google civic election id', blank=True)),
                ('candidate_url', models.URLField(null=True, verbose_name=b'website url of candidate campaign', blank=True)),
                ('facebook_url', models.URLField(null=True, verbose_name=b'facebook url of candidate campaign', blank=True)),
                ('twitter_url', models.URLField(null=True, verbose_name=b'twitter url of candidate campaign', blank=True)),
                ('google_plus_url', models.URLField(null=True, verbose_name=b'google plus url of candidate campaign', blank=True)),
                ('youtube_url', models.URLField(null=True, verbose_name=b'youtube url of candidate campaign', blank=True)),
                ('email', models.CharField(max_length=254, null=True, verbose_name=b'candidate campaign email', blank=True)),
                ('phone', models.CharField(max_length=254, null=True, verbose_name=b'candidate campaign email', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContestMeasure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('id_maplight', models.CharField(max_length=254, unique=True, null=True, verbose_name=b'maplight unique identifier', blank=True)),
                ('measure_title', models.CharField(max_length=254, verbose_name=b'measure title')),
                ('measure_subtitle', models.CharField(max_length=254, verbose_name=b'google civic referendum subtitle')),
                ('measure_url', models.CharField(max_length=254, null=True, verbose_name=b'measure details url')),
                ('election_id', models.CharField(max_length=254, verbose_name=b'we vote election id')),
                ('google_civic_election_id', models.CharField(max_length=254, verbose_name=b'election id')),
                ('primary_party', models.CharField(max_length=254, null=True, verbose_name=b'primary party', blank=True)),
                ('district_name', models.CharField(max_length=254, verbose_name=b'district name')),
                ('district_scope', models.CharField(max_length=254, verbose_name=b'district scope')),
                ('district_ocd_id', models.CharField(max_length=254, verbose_name=b'open civic data id')),
            ],
        ),
        migrations.CreateModel(
            name='ContestOffice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office_name', models.CharField(max_length=254, verbose_name=b'google civic office')),
                ('election_id', models.CharField(max_length=254, verbose_name=b'we vote election id')),
                ('google_civic_election_id', models.CharField(max_length=254, verbose_name=b'google civic election id')),
                ('id_cicero', models.CharField(max_length=254, unique=True, null=True, verbose_name=b'azavea cicero unique identifier', blank=True)),
                ('id_maplight', models.CharField(max_length=254, unique=True, null=True, verbose_name=b'maplight unique identifier', blank=True)),
                ('id_ballotpedia', models.CharField(max_length=254, null=True, verbose_name=b'ballotpedia unique identifier', blank=True)),
                ('id_wikipedia', models.CharField(max_length=254, null=True, verbose_name=b'wikipedia unique identifier', blank=True)),
                ('number_voting_for', models.CharField(max_length=254, null=True, verbose_name=b'number of candidates to vote for', blank=True)),
                ('number_elected', models.CharField(max_length=254, null=True, verbose_name=b'number of candidates who will be elected', blank=True)),
                ('primary_party', models.CharField(max_length=254, null=True, verbose_name=b'primary party', blank=True)),
                ('district_name', models.CharField(max_length=254, verbose_name=b'district name')),
                ('district_scope', models.CharField(max_length=254, verbose_name=b'district scope')),
                ('district_ocd_id', models.CharField(max_length=254, verbose_name=b'open civic data id')),
            ],
        ),
        migrations.CreateModel(
            name='Election',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('google_civic_election_id', models.CharField(max_length=20, unique=True, null=True, verbose_name=b'google civic election id')),
                ('name', models.CharField(max_length=254, verbose_name=b'election name')),
                ('election_date_text', models.CharField(max_length=254, verbose_name=b'election day')),
            ],
        ),
        migrations.CreateModel(
            name='MeasureCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contest_measure_id', models.CharField(max_length=254, verbose_name=b'contest_measure unique id')),
                ('stance', models.CharField(default=b'N', max_length=1, verbose_name=b'stance', choices=[(b'S', b'Support'), (b'N', b'Neutral'), (b'O', b'Oppose')])),
                ('candidate_name', models.CharField(max_length=254, verbose_name=b'candidate name')),
                ('party', models.CharField(max_length=254, null=True, verbose_name=b'party', blank=True)),
                ('photo_url', models.CharField(max_length=254, null=True, verbose_name=b'photoUrl', blank=True)),
                ('google_civic_election_id', models.CharField(max_length=254, verbose_name=b'google election id')),
                ('url', models.URLField(null=True, verbose_name=b'website url of campaign', blank=True)),
                ('facebook_url', models.URLField(null=True, verbose_name=b'facebook url of campaign', blank=True)),
                ('twitter_url', models.URLField(null=True, verbose_name=b'twitter url of campaign', blank=True)),
                ('google_plus_url', models.URLField(null=True, verbose_name=b'google plus url of campaign', blank=True)),
                ('youtube_url', models.URLField(null=True, verbose_name=b'youtube url of campaign', blank=True)),
                ('email', models.CharField(max_length=254, null=True, verbose_name=b'campaign email', blank=True)),
                ('phone', models.CharField(max_length=254, null=True, verbose_name=b'campaign email', blank=True)),
            ],
        ),
    ]
