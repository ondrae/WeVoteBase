# position/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-
# Diagrams here: https://docs.google.com/drawings/d/1DsPnl97GKe9f14h41RPeZDssDUztRETGkXGaolXCeyo/edit

from django.db import models
from election_office_measure.models import CandidateCampaign, MeasureCampaign
from exception.models import handle_exception, handle_exception_silently, handle_record_found_more_than_one_exception,\
    handle_record_not_found_exception, handle_record_not_saved_exception

from election_office_measure.models import CandidateCampaign
from twitter.models import TwitterUser
from django.contrib.auth.models import User
# from voter.models import Voter  # Replace User with this once we have figured out User -> Voter object linking

POSITION_CHOICES = (
    ('SUPPORT_STRONG',    'Strong Supports'),
    ('SUPPORT',           'Supports'),
    ('UNDECIDED',         'Undecided on'),
    ('NO_OPINION',        'No opinion'),
    ('OPPOSE',            'Opposes'),
    ('OPPOSE_STRONG',     'Strongly Opposes'),
)


class PositionEntered(models.Model):
    """
    Any position entered by any person gets its own PositionEntered entry. We then
    generate Position entries that get used to display an particular org's position.
    """
    # We are relying on built-in Python id field

    # The generated position that this PositionEntered entry influences
    position_id = models.BigIntegerField(null=True, blank=True)
    # The organization this position is for
    organization_id = models.BigIntegerField(null=True, blank=True)

    date_entered = models.DateTimeField(verbose_name='date entered', null=True)
    # The unique We Vote id of the tweet that is the source of the position
    tweet_source_id = models.BigIntegerField(null=True, blank=True)
    # This is the voter / authenticated user who entered the position
    voter_entering_position = models.ForeignKey(
        User, verbose_name='authenticated user who entered position', null=True, blank=True)
    # The Twitter user account that generated this position
    twitter_user_entered_position = models.ForeignKey(TwitterUser, null=True, verbose_name='')
    # This is the candidate/politician that the position refers to.
    #  Either candidate_campaign is filled OR measure_campaign, but not both
    # candidate_campaign = models.ForeignKey(
    #     CandidateCampaign, verbose_name='candidate campaign', null=True, blank=True,
    #     related_name='positionentered_candidate')
    candidate_campaign_id = models.BigIntegerField(verbose_name='id of candidate_campaign', null=True, blank=True)
    # Useful for queries based on Politicians -- not the main table we use for ballot display though
    politician_id = models.BigIntegerField(verbose_name='', null=True, blank=True)

    # This is the measure/initiative/proposition that the position refers to.
    #  Either measure_campaign is filled OR candidate_campaign, but not both
    # measure_campaign = models.ForeignKey(
    #  MeasureCampaign, verbose_name='measure campaign', null=True, blank=True, related_name='positionentered_measure')
    measure_campaign_id = models.BigIntegerField(verbose_name='id of measure_campaign', null=True, blank=True)

    # Strategic denormalization - this is redundant but will make generating the voter guide easier.
    # geo = models.ForeignKey(Geo, null=True, related_name='pos_geo')
    # issue = models.ForeignKey(Issue, null=True, blank=True, related_name='')

    stance = models.CharField(max_length=15, choices=POSITION_CHOICES, default='NO_OPINION')  # supporting/opposing

    statement_text = models.TextField(null=True, blank=True,)
    statement_html = models.TextField(null=True, blank=True,)
    # A link to any location with more information about this position
    more_info_url = models.URLField(blank=True, null=True, verbose_name='url with more info about this position')

    # Did this position come from a web scraper?
    from_scraper = models.BooleanField(default=False)
    # Was this position certified by an official with the organization?
    organization_certified = models.BooleanField(default=False)
    # Was this position certified by an official We Vote volunteer?
    volunteer_certified = models.BooleanField(default=False)

    # link = models.URLField(null=True, blank=True,)
    # link_title = models.TextField(null=True, blank=True, max_length=128)
    # link_site = models.TextField(null=True, blank=True, max_length=64)
    # link_txt = models.TextField(null=True, blank=True)
    # link_img = models.URLField(null=True, blank=True)
    # Set this to True after getting all the link details (title, txt, img etc)
    # details_loaded = models.BooleanField(default=False)
    # video_embed = models.URLField(null=True, blank=True)
    # spam_flag = models.BooleanField(default=False)
    # abuse_flag = models.BooleanField(default=False)
    # orig_json = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('date_entered',)

    def candidate_campaign(self):
        try:
            candidate_campaign = CandidateCampaign.objects.get(id=self.candidate_campaign_id)
        except CandidateCampaign.MultipleObjectsReturned as e:
            handle_record_found_more_than_one_exception(e)
            print "position.candidate_campaign Found multiple"
            return None
        except CandidateCampaign.DoesNotExist as e:
            handle_exception_silently(e)
            print "position.candidate_campaign did not find"
            return None
        print "Found candidate campaign"
        return candidate_campaign


class Position(models.Model):
    """
    This is a table of data generated from PositionEntered. Not all fields copied over from PositionEntered
    """
    # We are relying on built-in Python id field

    # The PositionEntered entry that was copied into this entry based on verification rules
    position_entered_id = models.BigIntegerField(null=True, blank=True)
    date_entered = models.DateTimeField(verbose_name='date entered', null=True)
    # The organization this position is for
    organization_id = models.BigIntegerField(null=True, blank=True)

    candidate_campaign = models.ForeignKey(
        CandidateCampaign, verbose_name='candidate campaign', null=True, blank=True, related_name='position_candidate')

    # Useful for queries based on Politicians -- not the main table we use for ballot display though
    politician_id = models.BigIntegerField(verbose_name='', null=True, blank=True)
    # This is the measure/initiative/proposition that the position refers to.
    #  Either measure_campaign is filled OR candidate_campaign, but not both
    measure_campaign = models.ForeignKey(
        MeasureCampaign, verbose_name='measure campaign', null=True, blank=True, related_name='position_measure')

    stance = models.CharField(max_length=15, choices=POSITION_CHOICES)  # supporting/opposing

    statement_text = models.TextField(null=True, blank=True,)
    statement_html = models.TextField(null=True, blank=True,)
    # A link to any location with more information about this position
    more_info_url = models.URLField(blank=True, null=True, verbose_name='url with more info about this position')

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('date_entered',)

    # def display_ballot_item_name(self):
    #     """
    #     Organization supports 'ballot_item_name' (which could be a campaign name, or measure name
    #     :return:
    #     """
    #     # Try to retrieve the candidate_campaign
    #     if candidate_campaign.id:
