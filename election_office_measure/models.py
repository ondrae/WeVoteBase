# election_office_measure/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.db import models
from exception.models import handle_exception, handle_exception_silently, handle_record_found_more_than_one_exception,\
    handle_record_not_found_exception, handle_record_not_saved_exception
# from position.models import PositionEntered


class Election(models.Model):
    # The unique ID of this election. (Provided by Google Civic)
    google_civic_election_id = models.CharField(verbose_name="google civic election id",
                                                max_length=20, null=True, unique=True)
    # A displayable name for the election.
    name = models.CharField(verbose_name="election name", max_length=254, null=False, blank=False)
    # Day of the election in YYYY-MM-DD format.
    election_date_text = models.CharField(verbose_name="election day", max_length=254, null=False, blank=False)


class ContestOffice(models.Model):
    # The name of the office for this contest.
    office_name = models.CharField(verbose_name="google civic office", max_length=254, null=False, blank=False)
    # The We Vote unique id for the election
    election_id = models.CharField(verbose_name="we vote election id", max_length=254, null=False, blank=False)
    # The unique ID of the election containing this contest. (Provided by Google Civic)
    google_civic_election_id = models.CharField(verbose_name="google civic election id",
                                                max_length=254, null=False, blank=False)
    id_cicero = models.CharField(
        verbose_name="azavea cicero unique identifier", max_length=254, null=True, blank=True, unique=True)
    id_maplight = models.CharField(
        verbose_name="maplight unique identifier", max_length=254, null=True, blank=True, unique=True)
    id_ballotpedia = models.CharField(
        verbose_name="ballotpedia unique identifier", max_length=254, null=True, blank=True)
    id_wikipedia = models.CharField(verbose_name="wikipedia unique identifier", max_length=254, null=True, blank=True)
    # vote_type (ranked choice, majority)

    # ballot_placement: NOTE - even though GoogleCivicContestOffice has this field, we store this value
    #  in the BallotItemCache table instead because it is different for each voter

    # The number of candidates that a voter may vote for in this contest.
    number_voting_for = models.CharField(verbose_name="number of candidates to vote for",
                                         max_length=254, null=True, blank=True)
    # The number of candidates that will be elected to office in this contest.
    number_elected = models.CharField(verbose_name="number of candidates who will be elected",
                                      max_length=254, null=True, blank=True)
    # If this is a partisan election, the name of the party it is for.
    primary_party = models.CharField(verbose_name="primary party", max_length=254, null=True, blank=True)
    # The name of the district.
    district_name = models.CharField(verbose_name="district name", max_length=254, null=False, blank=False)
    # The geographic scope of this district. If unspecified the district's geography is not known.
    # One of: national, statewide, congressional, stateUpper, stateLower, countywide, judicial, schoolBoard,
    # cityWide, township, countyCouncil, cityCouncil, ward, special
    district_scope = models.CharField(verbose_name="district scope", max_length=254, null=False, blank=False)
    # An identifier for this district, relative to its scope. For example, the 34th State Senate district
    # would have id "34" and a scope of stateUpper.
    district_ocd_id = models.CharField(verbose_name="open civic data id", max_length=254, null=False, blank=False)


class CandidateCampaign(models.Model):
    # election link to local We Vote Election entry. During setup we need to allow this to be null.
    election_id = models.IntegerField(verbose_name="election unique identifier", null=True, blank=True)
    # The internal We Vote id for the ContestOffice that this candidate is competing for.
    # During setup we need to allow this to be null.
    contest_office_id = models.CharField(
        verbose_name="contest_office_id id", max_length=254, null=True, blank=True)
    # politician link to local We Vote Politician entry. During setup we need to allow this to be null.
    politician_id = models.IntegerField(verbose_name="politician unique identifier", null=True, blank=True)
    # The candidate's name.
    candidate_name = models.CharField(verbose_name="candidate name", max_length=254, null=False, blank=False)
    # The full name of the party the candidate is a member of.
    party = models.CharField(verbose_name="party", max_length=254, null=True, blank=True)
    # A URL for a photo of the candidate.
    photo_url = models.CharField(verbose_name="photoUrl", max_length=254, null=True, blank=True)
    # The order the candidate appears on the ballot for this contest.
    order_on_ballot = models.CharField(verbose_name="order on ballot", max_length=254, null=True, blank=True)
    # The unique ID of the election containing this contest. (Provided by Google Civic)
    google_civic_election_id = models.CharField(
        verbose_name="google civic election id", max_length=254, null=True, blank=True)
    # The URL for the candidate's campaign web site.
    candidate_url = models.URLField(verbose_name='website url of candidate campaign', blank=True, null=True)
    facebook_url = models.URLField(verbose_name='facebook url of candidate campaign', blank=True, null=True)
    twitter_url = models.URLField(verbose_name='twitter url of candidate campaign', blank=True, null=True)
    google_plus_url = models.URLField(verbose_name='google plus url of candidate campaign', blank=True, null=True)
    youtube_url = models.URLField(verbose_name='youtube url of candidate campaign', blank=True, null=True)
    # The email address for the candidate's campaign.
    email = models.CharField(verbose_name="candidate campaign email", max_length=254, null=True, blank=True)
    # The voice phone number for the candidate's campaign office.
    phone = models.CharField(verbose_name="candidate campaign email", max_length=254, null=True, blank=True)

    # def position_list(self):
    #     try:
    #         position_list = PositionEntered.objects.filter(candidate_campaign_id=self.id)
    #     except PositionEntered.MultipleObjectsReturned as e:
    #         handle_record_found_more_than_one_exception(e)
    #         print "candidate_campaign.position_list Found multiple"
    #         return None
    #     except PositionEntered.DoesNotExist as e:
    #         handle_exception_silently(e)
    #         print "candidate_campaign.position_list did not find"
    #         return None
    #     print "Found candidate campaign. position_list"
    #     return position_list


class ContestMeasure(models.Model):
    id_maplight = models.CharField(verbose_name="maplight unique identifier",
                                   max_length=254, null=True, blank=True, unique=True)
    # The title of the measure (e.g. 'Proposition 42').
    measure_title = models.CharField(verbose_name="measure title", max_length=254, null=False, blank=False)
    # A brief description of the referendum. This field is only populated for contests of type 'Referendum'.
    measure_subtitle = models.CharField(verbose_name="google civic referendum subtitle",
                                        max_length=254, null=False, blank=False)
    # A link to the referendum. This field is only populated for contests of type 'Referendum'.
    measure_url = models.CharField(verbose_name="measure details url", max_length=254, null=True, blank=False)
    # The We Vote unique id for the election
    election_id = models.CharField(verbose_name="we vote election id", max_length=254, null=False, blank=False)
    # The unique ID of the election containing this contest. (Provided by Google Civic)
    google_civic_election_id = models.CharField(verbose_name="election id", max_length=254, null=False, blank=False)
    # ballot_placement: NOTE - even though GoogleCivicContestOffice has this field, we store this value
    #  in the BallotItemCache table instead because it is different for each voter
    # If this is a partisan election, the name of the party it is for.
    primary_party = models.CharField(verbose_name="primary party", max_length=254, null=True, blank=True)
    # The name of the district.
    district_name = models.CharField(verbose_name="district name", max_length=254, null=False, blank=False)
    # The geographic scope of this district. If unspecified the district's geography is not known.
    # One of: national, statewide, congressional, stateUpper, stateLower, countywide, judicial, schoolBoard,
    # cityWide, township, countyCouncil, cityCouncil, ward, special
    district_scope = models.CharField(verbose_name="district scope", max_length=254, null=False, blank=False)
    # An identifier for this district, relative to its scope. For example, the 34th State Senate district
    # would have id "34" and a scope of stateUpper.
    district_ocd_id = models.CharField(verbose_name="open civic data id", max_length=254, null=False, blank=False)


class MeasureCampaign(models.Model):
    # contest_measure link
    # The internal We Vote id for the ContestMeasure that this campaign taking a stance on
    contest_measure_id = models.CharField(verbose_name="contest_measure unique id",
                                          max_length=254, null=False, blank=False)
    # Is the campaign attempting to pass the measure, or stop it from passing?
    SUPPORT = 'S'
    NEUTRAL = 'N'
    OPPOSE = 'O'
    STANCE_CHOICES = (
        (SUPPORT, 'Support'),
        (NEUTRAL, 'Neutral'),
        (OPPOSE, 'Oppose'),
    )
    stance = models.CharField("stance", max_length=1, choices=STANCE_CHOICES, default=NEUTRAL)

    # The candidate's name.
    candidate_name = models.CharField(verbose_name="candidate name", max_length=254, null=False, blank=False)
    # The full name of the party the candidate is a member of.
    party = models.CharField(verbose_name="party", max_length=254, null=True, blank=True)
    # A URL for a photo of the candidate.
    photo_url = models.CharField(verbose_name="photoUrl", max_length=254, null=True, blank=True)
    # The unique ID of the election containing this contest. (Provided by Google Civic)
    google_civic_election_id = models.CharField(verbose_name="google election id",
                                                max_length=254, null=False, blank=False)
    # The URL for the candidate's campaign web site.
    url = models.URLField(verbose_name='website url of campaign', blank=True, null=True)
    facebook_url = models.URLField(verbose_name='facebook url of campaign', blank=True, null=True)
    twitter_url = models.URLField(verbose_name='twitter url of campaign', blank=True, null=True)
    google_plus_url = models.URLField(verbose_name='google plus url of campaign', blank=True, null=True)
    youtube_url = models.URLField(verbose_name='youtube url of campaign', blank=True, null=True)
    # The email address for the candidate's campaign.
    email = models.CharField(verbose_name="campaign email", max_length=254, null=True, blank=True)
    # The voice phone number for the campaign office.
    phone = models.CharField(verbose_name="campaign email", max_length=254, null=True, blank=True)


class BallotItemCache(models.Model):
    """
    This is a generated table from Google Civic data (and Azavea Cicero in the future)
    """
    # The unique id of the voter   # TODO temp default
    voter_id = models.IntegerField(verbose_name="the voter unique id", default=1, null=False, blank=False)
    # The We Vote unique ID of this election
    election_id = models.CharField(verbose_name="election id", max_length=20, null=True)
    # The unique ID of this election. (Provided by Google Civic)
    google_civic_election_id = models.CharField(verbose_name="google civic election id", max_length=20, null=True)
    # The internal We Vote id for the ContestOffice that this candidate is competing for
    contest_office_id = models.CharField(verbose_name="contest_office_id id", max_length=254, null=True, blank=True)
    # The internal We Vote id for the ContestMeasure that this campaign taking a stance on
    contest_measure_id = models.CharField(
        verbose_name="contest_measure unique id", max_length=254, null=True, blank=True)
    ballot_order = models.SmallIntegerField(
        verbose_name="the order this item should appear on the ballot", null=True, blank=True)
    # This is a sortable name
    ballot_item_label = models.CharField(verbose_name="a label we can sort by", max_length=254, null=True, blank=True)

    def is_contest_office(self):
        if self.contest_office_id:
            return True
        return False

    def is_contest_measure(self):
        if self.contest_measure_id:
            return True
        return False

    def display_ballot_item(self):
        return self.ballot_item_label

    def candidates_list(self):
        candidates_list_temp = CandidateCampaign.objects.all()
        candidates_list_temp = candidates_list_temp.filter(election_id=self.election_id)
        candidates_list_temp = candidates_list_temp.filter(contest_office_id=self.contest_office_id)
        return candidates_list_temp


# NOTE: This method only needs to hit the database at most once per day.
# We should cache the results in a JSON file that gets cached on the server and locally in the
# voter's browser for speed.
def retrieve_my_ballot(voter_on_stage, election_on_stage):
    # Retrieve all of the jurisdictions the voter is in

    # Retrieve all of the office_contests in each of those jurisdictions

    # Retrieve all of the measure_contests in each of those jurisdictions
    return True

