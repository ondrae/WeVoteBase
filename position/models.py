# position/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-
# Diagrams here: https://docs.google.com/drawings/d/1DsPnl97GKe9f14h41RPeZDssDUztRETGkXGaolXCeyo/edit

from django.db import models
from election_office_measure.models import CandidateCampaign, MeasureCampaign
from exception.models import handle_exception, handle_exception_silently, handle_record_found_more_than_one_exception,\
    handle_record_not_found_exception, handle_record_not_saved_exception
from organization.models import Organization
from twitter.models import TwitterUser
from voter.models import Voter
from wevote_settings.models import fetch_next_id_we_vote_last_position_integer, fetch_site_unique_id_prefix

ANY = 'ANY'  # This is a way to indicate when we want to return any stance (support, oppose, no_stance)
SUPPORT = 'SUPPORT'
STILL_DECIDING = 'STILL_DECIDING'
NO_STANCE = 'NO_STANCE'
INFORMATION_ONLY = 'INFO_ONLY'
OPPOSE = 'OPPOSE'
POSITION_CHOICES = (
    # ('SUPPORT_STRONG',    'Strong Supports'),  # I do not believe we will be offering 'SUPPORT_STRONG' as an option
    (SUPPORT,           'Supports'),
    (STILL_DECIDING,    'Still deciding'),
    (NO_STANCE,         'No stance'),
    (INFORMATION_ONLY,  'Information only'),
    (OPPOSE,            'Opposes'),
    # ('OPPOSE_STRONG',     'Strongly Opposes'),  # I do not believe we will be offering 'OPPOSE_STRONG' as an option
)


class PositionEntered(models.Model):
    """
    Any position entered by any person gets its own PositionEntered entry. We then
    generate Position entries that get used to display an particular org's position.
    """
    # We are relying on built-in Python id field

    # The id_we_vote identifier is unique across all We Vote sites, and allows us to share our org info with other
    # organizations
    # It starts with "wv" then we add on a database specific identifier like "3v" (WeVoteSetting.site_unique_id_prefix)
    # then the string "pos", and then a sequential integer like "123".
    # We keep the last value in WeVoteSetting.id_we_vote_last_position_integer
    id_we_vote = models.CharField(
        verbose_name="we vote permanent id", max_length=255, default=None, null=True, blank=True, unique=True)

    # The id for the generated position that this PositionEntered entry influences
    position_id = models.BigIntegerField(null=True, blank=True)

    date_entered = models.DateTimeField(verbose_name='date entered', null=True)
    # The organization this position is for
    organization_id = models.BigIntegerField(null=True, blank=True)

    # The voter expressing the opinion
    voter_id = models.BigIntegerField(null=True, blank=True)
    # The election this position is for
    election_id = models.BigIntegerField(verbose_name='election id', null=True, blank=True)

    # The unique We Vote id of the tweet that is the source of the position
    tweet_source_id = models.BigIntegerField(null=True, blank=True)
    # This is the voter / authenticated user who entered the position for an organization
    #  (NOT the voter expressing opinion)
    voter_entering_position = models.ForeignKey(
        Voter, verbose_name='authenticated user who entered position', null=True, blank=True)
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

    stance = models.CharField(max_length=15, choices=POSITION_CHOICES, default=NO_STANCE)  # supporting/opposing

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
        return self.stance

    class Meta:
        ordering = ('date_entered',)

    # We override the save function so we can auto-generate id_we_vote
    def save(self, *args, **kwargs):
        # Even if this organization came from another source we still need a unique id_we_vote
        if self.id_we_vote:
            self.id_we_vote = self.id_we_vote.strip()
        if self.id_we_vote == "" or self.id_we_vote is None:  # If there isn't a value...
            # ...generate a new id
            site_unique_id_prefix = fetch_site_unique_id_prefix()
            next_local_integer = fetch_next_id_we_vote_last_position_integer()
            # "wv" = We Vote
            # site_unique_id_prefix = a generated (or assigned) unique id for one server running We Vote
            # "pos" = tells us this is a unique id for an pos
            # next_integer = a unique, sequential integer for this server - not necessarily tied to database id
            self.id_we_vote = "wv{site_unique_id_prefix}pos{next_integer}".format(
                site_unique_id_prefix=site_unique_id_prefix,
                next_integer=next_local_integer,
            )
        super(PositionEntered, self).save(*args, **kwargs)

    def is_support(self):
        if self.stance == SUPPORT:
            return True
        return False

    def is_oppose(self):
        if self.stance == OPPOSE:
            return True
        return False

    def is_no_stance(self):
        if self.stance == NO_STANCE:
            return True
        return False

    def is_information_only(self):
        if self.stance == INFORMATION_ONLY:
            return True
        return False

    def is_still_deciding(self):
        if self.stance == STILL_DECIDING:
            return True
        return False

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
        return candidate_campaign

    def organization(self):
        try:
            organization = Organization.objects.get(id=self.organization_id)
        except Organization.MultipleObjectsReturned as e:
            handle_record_found_more_than_one_exception(e)
            print "position.candidate_campaign Found multiple"
            return None
        except Organization.DoesNotExist as e:
            handle_exception_silently(e)
            print "position.candidate_campaign did not find"
            return None
        return organization

    def organization_id_we_vote(self):
        try:
            organization_on_stage = Organization.objects.get(id=self.organization_id)
            if organization_on_stage.id_we_vote:
                return organization_on_stage.id_we_vote
        except Exception as e:
            handle_exception_silently(e)
        return ''

    def candidate_campaign_id_we_vote(self):
        try:
            candidate_campaign_on_stage = CandidateCampaign.objects.get(id=self.candidate_campaign_id)
            if candidate_campaign_on_stage.id_we_vote:
                return candidate_campaign_on_stage.id_we_vote
        except Exception as e:
            handle_exception_silently(e)
        return ''

    def measure_campaign_id_we_vote(self):
        try:
            measure_campaign_on_stage = Organization.objects.get(id=self.measure_campaign_id)
            if measure_campaign_on_stage.id_we_vote:
                return measure_campaign_on_stage.id_we_vote
        except Exception as e:
            handle_exception_silently(e)
        return ''


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
    # The election this position is for
    election_id = models.BigIntegerField(verbose_name='election id', null=True, blank=True)

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


class PositionListForCandidateCampaign(models.Model):
    """
    A way to retrieve all of the positions stated about this CandidateCampaign
    """
    # candidate_campaign = models.ForeignKey(
    #     CandidateCampaign, null=False, blank=False, verbose_name='candidate campaign')
    # position = models.ForeignKey(
    #     PositionEntered, null=False, blank=False, verbose_name='position about candidate')
    def retrieve_all_positions_for_candidate_campaign(self, candidate_campaign_id, stance_we_are_looking_for):
        # TODO Error check stance_we_are_looking_for

        # Note that one of the incoming options for stance_we_are_looking_for is 'ANY' which means we want to return
        #  all stances

        # Retrieve the support positions for this candidate_campaign_id
        organization_position_list = PositionEntered()
        organization_position_list_found = False
        try:
            organization_position_list = PositionEntered.objects.order_by('date_entered')
            organization_position_list = organization_position_list.filter(candidate_campaign_id=candidate_campaign_id)
            # SUPPORT, STILL_DECIDING, INFORMATION_ONLY, NO_STANCE, OPPOSE
            if stance_we_are_looking_for != ANY:
                # If we passed in the stance "ANY" it means we want to not filter down the list
                organization_position_list = organization_position_list.filter(stance=stance_we_are_looking_for)
            # organization_position_list = organization_position_list.filter(election_id=election_id)
            if len(organization_position_list):
                organization_position_list_found = True
        except Exception as e:
            handle_record_not_found_exception(e)

        if organization_position_list_found:
            return organization_position_list
        else:
            organization_position_list = {}
            return organization_position_list

    def calculate_positions_followed_by_voter(
            self, voter_id, all_positions_list_for_candidate_campaign, organizations_followed_by_voter):
        """
        We need a list of positions that were made by an organization that this voter follows
        :param all_positions_list_for_candidate_campaign:
        :param organizations_followed_by_voter:
        :return:
        """

        positions_followed_by_voter = []
        # Only return the positions if they are from organizations the voter follows
        for position in all_positions_list_for_candidate_campaign:
            if position.voter_id == voter_id:  # We include the voter currently viewing the ballot in this list
                positions_followed_by_voter.append(position)
            # TODO Include a check against a list of "people_followed_by_voter" so we can include friends
            elif position.organization_id in organizations_followed_by_voter:
                # print "position {position_id} followed by voter (org {org_id})".format(
                #     position_id=position.id, org_id=position.organization_id)
                positions_followed_by_voter.append(position)

        return positions_followed_by_voter

    def calculate_positions_not_followed_by_voter(
            self, all_positions_list_for_candidate_campaign, organizations_followed_by_voter):
        """
        We need a list of positions that were made by an organization that this voter follows
        :param all_positions_list_for_candidate_campaign:
        :param organizations_followed_by_voter:
        :return:
        """
        positions_not_followed_by_voter = []
        # Only return the positions if they are from organizations the voter follows
        for position in all_positions_list_for_candidate_campaign:
            # Some positions are for individual voters, so we want to filter those out
            if position.organization_id \
                    and position.organization_id not in organizations_followed_by_voter:
                # print "position {position_id} NOT followed by voter (org {org_id})".format(
                #     position_id=position.id, org_id=position.organization_id)
                positions_not_followed_by_voter.append(position)

        return positions_not_followed_by_voter


class PositionEnteredManager(models.Model):

    def __unicode__(self):
        return "PositionEnteredManager"

    def retrieve_organization_candidate_campaign_position(self, organization_id, candidate_campaign_id):
        """
        Find a position based on the organization_id & candidate_campaign_id
        :param organization_id:
        :param candidate_campaign_id:
        :return:
        """
        position_id = 0
        voter_id = 0
        measure_campaign_id = 0
        position_entered_manager = PositionEnteredManager()
        return position_entered_manager.retrieve_position(
            position_id, organization_id, voter_id, candidate_campaign_id, measure_campaign_id)

    def retrieve_voter_candidate_campaign_position(self, voter_id, candidate_campaign_id):
        organization_id = 0
        position_id = 0
        measure_campaign_id = 0
        position_entered_manager = PositionEnteredManager()
        return position_entered_manager.retrieve_position(
            position_id, organization_id, voter_id, candidate_campaign_id, measure_campaign_id)

    def retrieve_position_from_id(self, position_id):
        organization_id = 0
        voter_id = 0
        candidate_campaign_id = 0
        measure_campaign_id = 0
        position_entered_manager = PositionEnteredManager()
        return position_entered_manager.retrieve_position(
            position_id, organization_id, voter_id, candidate_campaign_id, measure_campaign_id)

    def retrieve_position(self, position_id, organization_id, voter_id, candidate_campaign_id, measure_campaign_id):
        error_result = False
        exception_does_not_exist = False
        exception_multiple_object_returned = False
        position_on_stage = PositionEntered()

        try:
            if position_id > 0:
                position_on_stage = PositionEntered.objects.get(id=position_id)
                position_id = position_on_stage.id
            elif organization_id > 0 and candidate_campaign_id > 0:
                position_on_stage = PositionEntered.objects.get(
                    organization_id=organization_id, candidate_campaign_id=candidate_campaign_id)
                # If still here, we found an existing position
                position_id = position_on_stage.id
            elif organization_id > 0 and measure_campaign_id > 0:
                position_on_stage = PositionEntered.objects.get(
                    organization_id=organization_id, measure_campaign_id=measure_campaign_id)
                position_id = position_on_stage.id
            elif voter_id > 0 and candidate_campaign_id > 0:
                position_on_stage = PositionEntered.objects.get(
                    voter_id=voter_id, candidate_campaign_id=candidate_campaign_id)
                position_id = position_on_stage.id
            elif voter_id > 0 and measure_campaign_id > 0:
                position_on_stage = PositionEntered.objects.get(
                    voter_id=voter_id, measure_campaign_id=measure_campaign_id)
                position_id = position_on_stage.id
        except PositionEntered.MultipleObjectsReturned as e:
            handle_record_found_more_than_one_exception(e)
            error_result = True
            exception_multiple_object_returned = True
        except PositionEntered.DoesNotExist as e:
            handle_exception_silently(e)
            error_result = True
            exception_does_not_exist = True

        results = {
            'error_result':             error_result,
            'DoesNotExist':             exception_does_not_exist,
            'MultipleObjectsReturned':  exception_multiple_object_returned,
            'position_found':           True if position_id > 0 else False,
            'position_id':              position_id,
            'position':                 position_on_stage,
            'is_support':               position_on_stage.is_support(),
            'is_oppose':                position_on_stage.is_oppose(),
            'is_no_stance':             position_on_stage.is_no_stance(),
            'is_information_only':      position_on_stage.is_information_only(),
            'is_still_deciding':        position_on_stage.is_still_deciding(),
        }
        return results

    def toggle_on_voter_support_for_candidate_campaign(self, voter_id, candidate_campaign_id):
        stance = SUPPORT
        position_entered_manager = PositionEnteredManager()
        return position_entered_manager.toggle_on_voter_position_for_candidate_campaign(
            voter_id, candidate_campaign_id, stance)

    def toggle_off_voter_support_for_candidate_campaign(self, voter_id, candidate_campaign_id):
        stance = NO_STANCE
        position_entered_manager = PositionEnteredManager()
        return position_entered_manager.toggle_on_voter_position_for_candidate_campaign(
            voter_id, candidate_campaign_id, stance)

    def toggle_on_voter_oppose_for_candidate_campaign(self, voter_id, candidate_campaign_id):
        stance = OPPOSE
        position_entered_manager = PositionEnteredManager()
        return position_entered_manager.toggle_on_voter_position_for_candidate_campaign(
            voter_id, candidate_campaign_id, stance)

    def toggle_off_voter_oppose_for_candidate_campaign(self, voter_id, candidate_campaign_id):
        stance = NO_STANCE
        position_entered_manager = PositionEnteredManager()
        return position_entered_manager.toggle_on_voter_position_for_candidate_campaign(
            voter_id, candidate_campaign_id, stance)

    def toggle_on_voter_position_for_candidate_campaign(self, voter_id, candidate_campaign_id, stance):
        # Does a position from this voter already exist?
        position_entered_manager = PositionEnteredManager()
        results = position_entered_manager.retrieve_voter_candidate_campaign_position(voter_id, candidate_campaign_id)

        voter_position_on_stage_found = False
        position_id = 0
        if results['position_found']:
            voter_position_on_stage = results['position']

            # Update this position with new values
            try:
                voter_position_on_stage.stance = stance
                # voter_position_on_stage.statement_text = statement_text
                voter_position_on_stage.save()
                position_id = voter_position_on_stage.id
                voter_position_on_stage_found = True
            except Exception as e:
                handle_record_not_saved_exception(e)

        elif results['MultipleObjectsReturned']:
            print "delete all but one and take it over?"
        elif results['DoesNotExist']:
            try:
                # Create new
                voter_position_on_stage = PositionEntered(
                    voter_id=voter_id,
                    candidate_campaign_id=candidate_campaign_id,
                    stance=stance,
                    #  statement_text=statement_text,
                )
                voter_position_on_stage.save()
                position_id = voter_position_on_stage.id
                voter_position_on_stage_found = True
            except Exception as e:
                handle_record_not_saved_exception(e)

        results = {
            'success':                  True if voter_position_on_stage_found else False,
            'position_id':              position_id,
            'position':                 voter_position_on_stage,
        }
        return results
