# region_jurisdiction/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.db import models


class Jurisdiction(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name
