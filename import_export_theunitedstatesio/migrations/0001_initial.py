# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TheUnitedStatesIoLegislatorCurrent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('last_name', models.CharField(default=None, max_length=254, null=True, verbose_name=b'last_name', blank=True)),
                ('first_name', models.CharField(default=None, max_length=254, null=True, verbose_name=b'first_name', blank=True)),
                ('birthday', models.DateField(default=None, null=True, verbose_name=b'birthday', blank=True)),
                ('gender', models.CharField(max_length=10, verbose_name=b'gender')),
                ('type', models.CharField(max_length=254, verbose_name=b'type')),
                ('state', models.CharField(max_length=25, verbose_name=b'state')),
                ('district', models.CharField(max_length=254, verbose_name=b'district')),
                ('party', models.CharField(max_length=254, verbose_name=b'party')),
                ('url', models.CharField(max_length=254, verbose_name=b'url')),
                ('address', models.CharField(max_length=254, verbose_name=b'address')),
                ('phone', models.CharField(max_length=254, verbose_name=b'phone')),
                ('contact_form', models.CharField(max_length=254, verbose_name=b'contact_form')),
                ('rss_url', models.CharField(max_length=254, verbose_name=b'rss_url')),
                ('twitter', models.CharField(max_length=254, verbose_name=b'twitter')),
                ('facebook', models.CharField(max_length=254, verbose_name=b'facebook')),
                ('facebook_id', models.CharField(max_length=254, verbose_name=b'facebook_id')),
                ('youtube', models.CharField(max_length=254, verbose_name=b'youtube')),
                ('youtube_id', models.CharField(default=None, max_length=500, null=True, verbose_name=b'youtube_id', blank=True)),
                ('bioguide_id', models.CharField(max_length=200, unique=True, null=True, verbose_name=b'bioguide unique identifier')),
                ('thomas_id', models.CharField(max_length=200, unique=True, null=True, verbose_name=b'thomas unique identifier')),
                ('opensecrets_id', models.CharField(max_length=200, null=True, verbose_name=b'opensecrets unique identifier')),
                ('lis_id', models.CharField(max_length=200, null=True, verbose_name=b'lis unique identifier')),
                ('cspan_id', models.CharField(max_length=200, null=True, verbose_name=b'cspan unique identifier')),
                ('govtrack_id', models.CharField(max_length=200, unique=True, null=True, verbose_name=b'govtrack unique identifier')),
                ('votesmart_id', models.CharField(max_length=200, null=True, verbose_name=b'votesmart unique identifier')),
                ('ballotpedia_id', models.CharField(default=None, max_length=500, null=True, verbose_name=b'ballotpedia id', blank=True)),
                ('washington_post_id', models.CharField(max_length=200, null=True, verbose_name=b'washington post unique identifier')),
                ('icpsr_id', models.CharField(max_length=200, null=True, verbose_name=b'icpsr unique identifier')),
                ('wikipedia_id', models.CharField(default=None, max_length=500, null=True, verbose_name=b'wikipedia id', blank=True)),
                ('was_processed', models.BooleanField(default=False, verbose_name=b'is primary election')),
            ],
        ),
    ]
