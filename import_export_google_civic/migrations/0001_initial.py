# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoogleCivicCandidateCampaign',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name=b'google civic candidate name')),
                ('party', models.CharField(max_length=254, null=True, verbose_name=b'google civic party', blank=True)),
                ('photo_url', models.CharField(max_length=254, null=True, verbose_name=b'google civic photoUrl', blank=True)),
                ('order_on_ballot', models.CharField(max_length=254, null=True, verbose_name=b'google civic order on ballot', blank=True)),
                ('google_civic_contest_office_id', models.CharField(max_length=254, verbose_name=b'google civic internal temp contest_office_id id')),
                ('we_vote_contest_office_id', models.CharField(max_length=254, null=True, verbose_name=b'we vote contest_office_id id', blank=True)),
                ('google_civic_election_id', models.CharField(max_length=254, verbose_name=b'google election id')),
                ('we_vote_election_id', models.CharField(max_length=254, null=True, verbose_name=b'we vote election id', blank=True)),
                ('we_vote_candidate_campaign_id', models.CharField(max_length=254, null=True, verbose_name=b'we vote candidate campaign id', blank=True)),
                ('we_vote_politician_id', models.CharField(max_length=254, null=True, verbose_name=b'we vote politician id', blank=True)),
                ('candidate_url', models.URLField(null=True, verbose_name=b'website url of candidate campaign', blank=True)),
                ('facebook_url', models.URLField(null=True, verbose_name=b'facebook url of candidate campaign', blank=True)),
                ('twitter_url', models.URLField(null=True, verbose_name=b'twitter url of candidate campaign', blank=True)),
                ('google_plus_url', models.URLField(null=True, verbose_name=b'google plus url of candidate campaign', blank=True)),
                ('youtube_url', models.URLField(null=True, verbose_name=b'youtube url of candidate campaign', blank=True)),
                ('email', models.CharField(max_length=254, null=True, verbose_name=b'google civic candidate campaign email', blank=True)),
                ('phone', models.CharField(max_length=254, null=True, verbose_name=b'google civic candidate campaign email', blank=True)),
                ('was_processed', models.BooleanField(default=False, verbose_name=b'is primary election')),
            ],
        ),
        migrations.CreateModel(
            name='GoogleCivicContestOffice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('office', models.CharField(max_length=254, verbose_name=b'google civic office')),
                ('google_civic_election_id', models.CharField(max_length=254, null=True, verbose_name=b'google civic election id', blank=True)),
                ('we_vote_election_id', models.CharField(max_length=254, null=True, verbose_name=b'we vote election id', blank=True)),
                ('we_vote_contest_office_id', models.CharField(max_length=254, null=True, verbose_name=b'we vote contest office id', blank=True)),
                ('number_voting_for', models.CharField(max_length=254, null=True, verbose_name=b'google civic number of candidates to vote for', blank=True)),
                ('number_elected', models.CharField(max_length=254, null=True, verbose_name=b'google civic number of candidates who will be elected', blank=True)),
                ('contest_level0', models.CharField(max_length=254, null=True, verbose_name=b'google civic level, option 0', blank=True)),
                ('contest_level1', models.CharField(max_length=254, null=True, verbose_name=b'google civic level, option 1', blank=True)),
                ('contest_level2', models.CharField(max_length=254, null=True, verbose_name=b'google civic level, option 2', blank=True)),
                ('ballot_placement', models.CharField(max_length=254, null=True, verbose_name=b'google civic ballot placement', blank=True)),
                ('primary_party', models.CharField(max_length=254, null=True, verbose_name=b'google civic primary party', blank=True)),
                ('district_name', models.CharField(max_length=254, verbose_name=b'google civic district name')),
                ('district_scope', models.CharField(max_length=254, verbose_name=b'google civic district scope')),
                ('district_ocd_id', models.CharField(max_length=254, verbose_name=b'google civic district ocd id')),
                ('electorate_specifications', models.CharField(max_length=254, null=True, verbose_name=b'google civic primary party', blank=True)),
                ('special', models.CharField(max_length=254, null=True, verbose_name=b'google civic primary party', blank=True)),
                ('was_processed', models.BooleanField(default=False, verbose_name=b'is primary election')),
            ],
        ),
        migrations.CreateModel(
            name='GoogleCivicContestReferendum',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('referendum_title', models.CharField(max_length=254, verbose_name=b'google civic referendum title')),
                ('referendum_subtitle', models.CharField(max_length=254, verbose_name=b'google civic referendum subtitle')),
                ('referendum_url', models.CharField(max_length=254, null=True, verbose_name=b'google civic referendum details url')),
                ('google_civic_election_id', models.CharField(max_length=254, verbose_name=b'google civic election id')),
                ('we_vote_election_id', models.CharField(max_length=254, null=True, verbose_name=b'we vote election id', blank=True)),
                ('ballot_placement', models.CharField(max_length=254, null=True, verbose_name=b'google civic ballot placement', blank=True)),
                ('primary_party', models.CharField(max_length=254, null=True, verbose_name=b'google civic primary party', blank=True)),
                ('district_name', models.CharField(max_length=254, verbose_name=b'google civic district name')),
                ('district_scope', models.CharField(max_length=254, verbose_name=b'google civic district scope')),
                ('district_ocd_id', models.CharField(max_length=254, verbose_name=b'google civic district ocd id')),
                ('electorate_specifications', models.CharField(max_length=254, null=True, verbose_name=b'google civic primary party', blank=True)),
                ('special', models.CharField(max_length=254, null=True, verbose_name=b'google civic primary party', blank=True)),
                ('was_processed', models.BooleanField(default=False, verbose_name=b'is primary election')),
            ],
        ),
        migrations.CreateModel(
            name='GoogleCivicElection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('google_civic_election_id', models.CharField(unique=True, max_length=20, verbose_name=b'google civic election id')),
                ('we_vote_election_id', models.CharField(max_length=20, unique=True, null=True, verbose_name=b'we vote election id', blank=True)),
                ('name', models.CharField(max_length=254, verbose_name=b'google civic election name')),
                ('election_day', models.CharField(max_length=254, verbose_name=b'google civic election day')),
                ('was_processed', models.BooleanField(default=False, verbose_name=b'is primary election')),
            ],
        ),
    ]
