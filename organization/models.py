# organization/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.db import models
from position.models import Position


class Organization(models.Model):
    # We are relying on built-in Python id field
    name = models.CharField(
        verbose_name="first name", max_length=255, default=None, null=True, blank=True)
    url = models.URLField(verbose_name='url of the endorsing organization', blank=True, null=True)
    twitter_handle = models.CharField(max_length=15, null=True, unique=False, verbose_name='twitter handle')

    NONPROFIT_501C3 = '3'
    NONPROFIT_501C4 = '4'
    POLITICAL_ACTION_COMMITTEE = 'P'
    CORPORATION = 'C'
    NEWS_CORPORATION = 'N'
    UNKNOWN = 'U'
    ORGANIZATION_TYPE_CHOICES = (
        (NONPROFIT_501C3, 'Nonprofit 501c3'),
        (NONPROFIT_501C4, 'Nonprofit 501c4'),
        (POLITICAL_ACTION_COMMITTEE, 'Political Action Committee'),
        (CORPORATION, 'Corporation'),
        (NEWS_CORPORATION, 'News Corporation'),
        (UNKNOWN, 'Unknown'),
    )

    organization_type = models.CharField("type of org", max_length=1, choices=ORGANIZATION_TYPE_CHOICES, default=UNKNOWN)

    # Link to a logo for this organization
    # logo

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('name',)

    def is_nonprofit_501c3(self):
        return self.organization_type in self.NONPROFIT_501C3

    def is_nonprofit_501c4(self):
        return self.organization_type in self.NONPROFIT_501C4

    def is_political_action_committee(self):
        return self.organization_type in self.POLITICAL_ACTION_COMMITTEE

    def is_corporation(self):
        return self.organization_type in self.CORPORATION

    def is_news_corporation(self):
        return self.organization_type in self.NEWS_CORPORATION

    def is_organization_type_specified(self):
        return self.organization_type in (
            self.NONPROFIT_501C3, self.NONPROFIT_501C4, self.POLITICAL_ACTION_COMMITTEE,
            self.CORPORATION, self.NEWS_CORPORATION)


# class OrganizationPositionLink(models.Model):
#     """
#     A confirmed link between an Organization & a Position.
#     """
#     organization = models.ForeignKey(Organization, null=False, blank=False, verbose_name='organization')
#     position = models.ForeignKey(Position, null=False, blank=False, verbose_name='position')
