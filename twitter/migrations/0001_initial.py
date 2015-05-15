# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author_handle', models.CharField(max_length=15, verbose_name=b"twitter handle of this tweet's author")),
                ('is_retweet', models.BooleanField(default=False, verbose_name=b'is this a retweet?')),
                ('body', models.CharField(max_length=255, null=True, verbose_name=b'', blank=True)),
                ('date_published', models.DateTimeField(null=True, verbose_name=b'date published')),
            ],
        ),
        migrations.CreateModel(
            name='TweetFavorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('favorited_by_handle', models.CharField(max_length=15, verbose_name=b'twitter handle of person who favorited this tweet')),
                ('date_favorited', models.DateTimeField(null=True, verbose_name=b'date favorited')),
                ('tweet_id', models.ForeignKey(verbose_name=b'we vote tweet id', blank=True, to='twitter.Tweet', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handle', models.CharField(unique=True, max_length=15, verbose_name=b'twitter handle')),
                ('fullname', models.CharField(max_length=80, null=True, verbose_name=b'full name of twitter user', blank=True)),
                ('is_group', models.BooleanField(default=False, verbose_name=b'is this a twitter group account')),
                ('user_url', models.URLField(null=True, verbose_name=b"url of user's website", blank=True)),
                ('bio_statement', models.CharField(max_length=255, null=True, verbose_name=b'bio for user', blank=True)),
                ('icon_url', models.URLField(null=True, verbose_name=b"url of user's profile icon", blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TwitterWhoFollowMe',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handle_of_me', models.CharField(max_length=15, verbose_name=b"from this twitter handle's perspective...")),
                ('handle_that_follows_me', models.CharField(max_length=15, verbose_name=b"twitter handle of this tweet's author")),
            ],
        ),
        migrations.CreateModel(
            name='TwitterWhoIFollow',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('handle_of_me', models.CharField(max_length=15, verbose_name=b"from this twitter handle's perspective...")),
                ('handle_i_follow', models.CharField(max_length=15, verbose_name=b'twitter handle being followed')),
            ],
        ),
    ]
