# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Voter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('email', models.EmailField(unique=True, max_length=255, verbose_name=b'email address')),
                ('first_name', models.CharField(max_length=255, null=True, verbose_name=b'first name', blank=True)),
                ('last_name', models.CharField(max_length=255, null=True, verbose_name=b'last name', blank=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name=b'date joined')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('middle_name', models.CharField(max_length=255, null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
