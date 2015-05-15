# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Politician',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=None, max_length=255, null=True, verbose_name=b'first name', blank=True)),
                ('middle_name', models.CharField(default=None, max_length=255, null=True, verbose_name=b'middle name', blank=True)),
                ('last_name', models.CharField(default=None, max_length=255, null=True, verbose_name=b'last name', blank=True)),
                ('full_name_official', models.CharField(default=None, max_length=255, null=True, verbose_name=b'official full name', blank=True)),
                ('full_name_google_civic', models.CharField(default=None, max_length=255, null=True, verbose_name=b'full name from google civic', blank=True)),
                ('full_name_assembled', models.CharField(default=None, max_length=255, null=True, verbose_name=b'full name from google civic', blank=True)),
                ('gender', models.CharField(default=b'U', max_length=1, verbose_name=b'gender', choices=[(b'F', b'Female'), (b'N', b'Gender Neutral'), (b'M', b'Male'), (b'U', b'Unknown')])),
                ('birth_date', models.DateField(default=None, null=True, verbose_name=b'birth date', blank=True)),
                ('id_bioguide', models.CharField(max_length=200, unique=True, null=True, verbose_name=b'bioguide unique identifier')),
                ('id_thomas', models.CharField(max_length=200, unique=True, null=True, verbose_name=b'thomas unique identifier')),
                ('id_lis', models.CharField(max_length=200, null=True, verbose_name=b'lis unique identifier', blank=True)),
                ('id_govtrack', models.CharField(max_length=200, unique=True, null=True, verbose_name=b'govtrack unique identifier')),
                ('id_opensecrets', models.CharField(max_length=200, null=True, verbose_name=b'opensecrets unique identifier')),
                ('id_votesmart', models.CharField(max_length=200, null=True, verbose_name=b'votesmart unique identifier')),
                ('id_fec', models.CharField(max_length=200, unique=True, null=True, verbose_name=b'fec unique identifier', blank=True)),
                ('id_cspan', models.CharField(max_length=200, null=True, verbose_name=b'cspan unique identifier', blank=True)),
                ('id_wikipedia', models.CharField(default=None, max_length=500, null=True, verbose_name=b'wikipedia url', blank=True)),
                ('id_ballotpedia', models.CharField(default=None, max_length=500, null=True, verbose_name=b'ballotpedia url', blank=True)),
                ('id_house_history', models.CharField(max_length=200, null=True, verbose_name=b'house history unique identifier', blank=True)),
                ('id_maplight', models.CharField(max_length=200, unique=True, null=True, verbose_name=b'maplight unique identifier', blank=True)),
                ('id_washington_post', models.CharField(max_length=200, null=True, verbose_name=b'washington post unique identifier')),
                ('id_icpsr', models.CharField(max_length=200, null=True, verbose_name=b'icpsr unique identifier')),
                ('party', models.CharField(max_length=254, null=True, verbose_name=b'politician political party')),
                ('state_code', models.CharField(max_length=2, null=True, verbose_name=b'politician home state')),
            ],
            options={
                'ordering': ('last_name',),
            },
        ),
        migrations.CreateModel(
            name='PoliticianTagLink',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('politician', models.ForeignKey(verbose_name=b'politician unique identifier', to='politician.Politician')),
                ('tag', models.ForeignKey(verbose_name=b'tag unique identifier', to='tag.Tag')),
            ],
        ),
        migrations.CreateModel(
            name='PoliticianTagLinkDisputed',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('politician', models.ForeignKey(verbose_name=b'politician unique identifier', to='politician.Politician')),
                ('tag', models.ForeignKey(verbose_name=b'tag unique identifier', to='tag.Tag')),
            ],
        ),
        migrations.AddField(
            model_name='politician',
            name='tag_link',
            field=models.ManyToManyField(to='tag.Tag', through='politician.PoliticianTagLink'),
        ),
    ]
