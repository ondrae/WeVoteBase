# import_export_maplight/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from datetime import datetime
from django.db import models
from election_office_measure.models import CandidateCampaign, ContestOffice, ContestOfficeManager
from exception.models import handle_exception_silently, handle_record_found_more_than_one_exception, \
    handle_record_not_saved_exception
import json

def validate_maplight_date(d):
    try:
        datetime.strptime(d, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# TODO Also create MapLightContestMeasure
class MapLightContestOffice(models.Model):
    election_date = models.DateField('election date', default=None, null=True, blank=True)  # "2014-09-03"
    contest_id = models.CharField(
        verbose_name='contest id', max_length=255, null=False, blank=False, unique=True)  # "O1524"
    title = models.CharField(
        verbose_name='title', max_length=255, null=False, blank=False, unique=False)  # "Governor - California"
    type = models.CharField(
        verbose_name='type', max_length=255, null=False, blank=False, unique=False)  # "office"

    # "http://votersedge.org/california/2014/november/state/candidates/governor"
    url = models.CharField(verbose_name='url', max_length=255, null=False, blank=False, unique=False)


class MapLightContestOfficeManager(models.Model):

    def __unicode__(self):
        return "MapLightContestOfficeManager"

    def retrieve_maplight_contest_office_from_id(self, contest_office_id):
        maplight_contest_office_manager = MapLightContestOfficeManager()
        return maplight_contest_office_manager.retrieve_maplight_contest_office(contest_office_id)

    def fetch_maplight_contest_office_from_id_maplight(self, id_maplight):
        maplight_contest_office_manager = MapLightContestOfficeManager()
        results = maplight_contest_office_manager.retrieve_maplight_contest_office_from_id_maplight(id_maplight)
        if results['success']:
            return results['maplight_contest_office']
        return MapLightContestOffice()

    def retrieve_maplight_contest_office_from_id_maplight(self, id_maplight):
        contest_office_id = 0
        maplight_contest_office_manager = MapLightContestOfficeManager()
        return maplight_contest_office_manager.retrieve_maplight_contest_office(contest_office_id, id_maplight)

    def fetch_maplight_contest_office_id_from_id_maplight(self, id_maplight):
        contest_office_id = 0
        maplight_contest_office_manager = MapLightContestOfficeManager()
        results = maplight_contest_office_manager.retrieve_maplight_contest_office(contest_office_id, id_maplight)
        if results['success']:
            return results['maplight_contest_office_id']
        return 0

    # NOTE: searching by all other variables seems to return a list of objects
    def retrieve_maplight_contest_office(self, contest_office_id, id_maplight=None):
        error_result = False
        exception_does_not_exist = False
        exception_multiple_object_returned = False
        maplight_contest_office_on_stage = MapLightContestOffice()

        try:
            if contest_office_id > 0:
                maplight_contest_office_on_stage = MapLightContestOffice.objects.get(id=contest_office_id)
                contest_office_id = maplight_contest_office_on_stage.id
            elif len(id_maplight) > 0:
                maplight_contest_office_on_stage = MapLightContestOffice.objects.get(contest_id=id_maplight)
                contest_office_id = maplight_contest_office_on_stage.id
        except MapLightContestOffice.MultipleObjectsReturned as e:
            handle_record_found_more_than_one_exception(e)
            exception_multiple_object_returned = True
        except MapLightContestOffice.DoesNotExist as e:
            handle_exception_silently(e)
            exception_does_not_exist = True

        results = {
            'success':                          True if contest_office_id > 0 else False,
            'error_result':                     error_result,
            'DoesNotExist':                     exception_does_not_exist,
            'MultipleObjectsReturned':          exception_multiple_object_returned,
            'maplight_contest_office_found':    True if contest_office_id > 0 else False,
            'contest_office_id':                contest_office_id,
            'maplight_contest_office':          maplight_contest_office_on_stage,
        }
        return results


class MapLightCandidate(models.Model):
    candidate_id = models.IntegerField(verbose_name='candidate id', null=False, blank=False, unique=True)  # "5746"
    display_name = models.CharField(
        verbose_name='display name', max_length=255, null=False, blank=False, unique=False)  # "Jerry Brown"
    first_name = models.CharField(
        verbose_name='first name', max_length=255, null=False, blank=True, unique=False)
    models.CharField(
        verbose_name='display name', max_length=255, null=False, blank=False, unique=False)
    gender = models.CharField(
        verbose_name='gender', max_length=1, null=False, blank=False, default='U', unique=False)  # "M"
    last_funding_update = models.DateField(
        verbose_name='last funding update date', default=None, null=True, blank=True)  # "2014-09-03"
    last_name = models.CharField(
        verbose_name='last name', max_length=255, null=False, blank=True, unique=False)  # "Brown"
    middle_name = models.CharField(verbose_name='middle name', max_length=255, null=False, blank=False, unique=False)
    name_prefix = models.CharField(verbose_name='name prefix', max_length=255, null=False, blank=True, unique=False)
    name_suffix = models.CharField(verbose_name='name suffix', max_length=255, null=False, blank=True, unique=False)
    original_name = models.CharField(
        verbose_name='original name', max_length=255, null=False, blank=True, unique=False)  # "Edmund G Brown"
    party = models.CharField(
        verbose_name='political party', max_length=255, null=False, blank=True, unique=False)  # "Democratic"

    # "http://votersedge.org/sites/all/modules/map/modules/map_proposition/images/politicians/2633.jpg?v"
    photo = models.CharField(
        verbose_name='photo url', max_length=255, null=False, blank=True, unique=False)
    politician_id = models.IntegerField(verbose_name='politician id', null=False, blank=False, unique=True)  # "2633"
    roster_name = models.CharField(
        verbose_name='roster name', max_length=255, null=False, blank=True, unique=False)  # "Jerry Brown"
    type = models.CharField(verbose_name='type', max_length=255, null=False, blank=True, unique=False)

    # "http://votersedge.org/california/2014/november/state/candidates/governor/2633-jerry-brown"
    url = models.CharField(verbose_name='url', max_length=255, null=False, blank=True, unique=False)


class MapLightCandidateManager(models.Model):

    def __unicode__(self):
        return "MapLightCandidateManager"

    def retrieve_maplight_candidate_from_id(self, candidate_id):
        maplight_candidate_manager = MapLightCandidateManager()
        return maplight_candidate_manager.retrieve_maplight_candidate(candidate_id)

    def retrieve_maplight_candidate_from_candidate_id_maplight(self, candidate_id_maplight):
        candidate_id = 0
        politician_id_maplight = 0
        maplight_candidate_manager = MapLightCandidateManager()
        return maplight_candidate_manager.retrieve_maplight_candidate(
            candidate_id, candidate_id_maplight, politician_id_maplight)

    def fetch_maplight_candidate_from_candidate_id_maplight(self, candidate_id_maplight):
        maplight_candidate_manager = MapLightCandidateManager()
        results = maplight_candidate_manager.retrieve_maplight_candidate_from_candidate_id_maplight(
            candidate_id_maplight)
        if results['success']:
            return results['maplight_candidate']
        else:
            return MapLightCandidate()

    def retrieve_maplight_candidate_from_politician_id_maplight(self, politician_id_maplight):
        candidate_id = 0
        candidate_id_maplight = 0
        maplight_candidate_manager = MapLightCandidateManager()
        return maplight_candidate_manager.retrieve_maplight_candidate(
            candidate_id, candidate_id_maplight, politician_id_maplight)

    def fetch_maplight_candidate_from_politician_id_maplight(self, politician_id_maplight):
        maplight_candidate_manager = MapLightCandidateManager()
        results = maplight_candidate_manager.retrieve_maplight_candidate_from_politician_id_maplight(
            politician_id_maplight)
        if results['success']:
            return results['maplight_candidate']
        else:
            return MapLightCandidate()

    # NOTE: searching by all other variables seems to return a list of objects
    def retrieve_maplight_candidate(self, candidate_id, candidate_id_maplight=None, politician_id_maplight=None):
        error_result = False
        exception_does_not_exist = False
        exception_multiple_object_returned = False
        maplight_candidate_on_stage = MapLightCandidate()

        try:
            if candidate_id > 0:
                maplight_candidate_on_stage = MapLightCandidate.objects.get(id=candidate_id)
                candidate_id = maplight_candidate_on_stage.id
            elif len(candidate_id_maplight) > 0:
                maplight_candidate_on_stage = MapLightCandidate.objects.get(candidate_id=candidate_id_maplight)
                candidate_id = maplight_candidate_on_stage.id
            elif len(politician_id_maplight) > 0:
                maplight_candidate_on_stage = MapLightCandidate.objects.get(politician_id=politician_id_maplight)
                candidate_id = maplight_candidate_on_stage.id
        except MapLightCandidate.MultipleObjectsReturned as e:
            handle_record_found_more_than_one_exception(e)
            exception_multiple_object_returned = True
        except MapLightCandidate.DoesNotExist as e:
            handle_exception_silently(e)
            exception_does_not_exist = True

        results = {
            'success':                          True if candidate_id > 0 else False,
            'error_result':                     error_result,
            'DoesNotExist':                     exception_does_not_exist,
            'MultipleObjectsReturned':          exception_multiple_object_returned,
            'maplight_candidate_found':         True if candidate_id > 0 else False,
            'candidate_id':                     candidate_id,
            'maplight_candidate':               maplight_candidate_on_stage,
        }
        return results


MAPLIGHT_SAMPLE_BALLOT_JSON_FILE = "import_export_maplight/import_data/maplight_sf_ballot_sample.json"
MAPLIGHT_SAMPLE_CONTEST_JSON_FILE = "import_export_maplight/import_data/contest_{contest_id}.json"


def import_maplight_from_json(request):
    load_from_url = False
    ballot_for_one_voter_array = []
    if load_from_url:
        # Request json file from Maplight servers
        print "TO BE IMPLEMENTED: Load Maplight JSON from url"
        # request = requests.get(VOTER_INFO_URL, params={
        #     "key": GOOGLE_CIVIC_API_KEY,  # This comes from an environment variable
        #     "address": "254 Hartford Street San Francisco CA",
        #     "electionId": "2000",
        # })
        # structured_json = json.loads(request.text)
    else:
        # Load saved json from local file
        print "Loading Maplight sample JSON from local file"

        with open(MAPLIGHT_SAMPLE_BALLOT_JSON_FILE) as ballot_for_one_voter_json:
            ballot_for_one_voter_array = json.load(ballot_for_one_voter_json)

    # A MapLight ballot query is essentially an array of contests with the key as the contest_id
    if ballot_for_one_voter_array and len(ballot_for_one_voter_array):
        # Parse the JSON here. This JSON is a list of contests on the ballot for one voter.
        for contest_id in ballot_for_one_voter_array:
            # Get a description of the contest. Office? Measure?
            contest_overview_array = ballot_for_one_voter_array[contest_id]

            if contest_overview_array['type'] == "office":
                # Get a description of the office the candidates are competing for
                # contest_office_description_json = contest_overview_array['office']

                # With the contest_id, we can look up who is running
                politicians_running_for_one_contest_array = []
                if load_from_url:
                    print "TO BE IMPLEMENTED: Load MapLight JSON for a contest from URL"
                else:
                    json_file_with_the_data_from_this_contest = MAPLIGHT_SAMPLE_CONTEST_JSON_FILE.format(
                        contest_id=contest_id)
                    try:
                        with open(json_file_with_the_data_from_this_contest) as json_data:
                            politicians_running_for_one_contest_array = json.load(json_data)
                    except Exception as e:
                        handle_exception_silently(e)
                        print "File {file_path} not found.".format(file_path=json_file_with_the_data_from_this_contest)
                        # Don't try to process the file if it doesn't exist, but go to the next entry
                        continue
    
                import_maplight_contest_office_candidates_from_array(politicians_running_for_one_contest_array)

            # Also add measure
    return


def import_maplight_contest_office_candidates_from_array(politicians_running_for_one_contest_array):
    maplight_contest_office_saved = False  # Has the contest these politicians are running for been saved?
    maplight_contest_office_manager = MapLightContestOfficeManager()
    maplight_candidate_manager = MapLightCandidateManager()

    loop_count = 0
    loop_count_limit = 1

    for politician_id in politicians_running_for_one_contest_array:
        one_politician_array = politicians_running_for_one_contest_array[politician_id]

        # Save the office_contest so we can link the politicians to it first

        if not maplight_contest_office_saved:
            maplight_contest_office = MapLightContestOffice()
            if 'contest' in one_politician_array:
                maplight_contest_array = one_politician_array['contest']
                if 'office' in maplight_contest_array:
                    maplight_contest_office_array = maplight_contest_array['office']
                if 'id' in maplight_contest_array:
                    maplight_contest_id = maplight_contest_array['id']
                    maplight_contest_office = \
                        maplight_contest_office_manager.fetch_maplight_contest_office_from_id_maplight(
                            maplight_contest_id)

            # If an internal identifier is found, then we know we have an object
            if maplight_contest_office.id:
                maplight_contest_office_saved = True
                # try:
                #     maplight_contest_office.contest_id = maplight_contest_array['id']
                #     maplight_contest_office.election_date = maplight_contest_array['election_date']
                #     maplight_contest_office.title = maplight_contest_array['title']
                #     maplight_contest_office.type = maplight_contest_array['type']
                #     maplight_contest_office.url = maplight_contest_array['url']
                #     # Save into this db the 'office'?
                #     # Save into this db the 'jurisdiction'?
                #     maplight_contest_office.save()
                #     maplight_contest_office_saved = True
                #
                # except Exception as e:
                #     handle_record_not_saved_exception(e)
            else:
                try:
                    maplight_contest_office = MapLightContestOffice(
                        contest_id=maplight_contest_array['id'],
                        election_date=maplight_contest_array['election_date'],
                        title=maplight_contest_array['title'],
                        type=maplight_contest_array['type'],
                        url=maplight_contest_array['url'],
                    )
                    # Save into this db the 'office'?
                    # Save into this db the 'jurisdiction'?
                    maplight_contest_office.save()
                    maplight_contest_office_saved = True

                except Exception as e:
                    handle_record_not_saved_exception(e)

        maplight_candidate = maplight_candidate_manager.fetch_maplight_candidate_from_candidate_id_maplight(
            one_politician_array['candidate_id'])

        if maplight_candidate.id:
            print "Candidate {display_name} previously saved. To Update?".format(
                display_name=maplight_candidate.display_name)
        else:
            # Not found in the MapLightCandidate database, so we need to save
            try:
                maplight_candidate = MapLightCandidate()
                maplight_candidate.politician_id = one_politician_array['politician_id']
                maplight_candidate.candidate_id = one_politician_array['candidate_id']
                maplight_candidate.display_name = one_politician_array['display_name']
                maplight_candidate.original_name = one_politician_array['original_name']
                maplight_candidate.gender = one_politician_array['gender']
                maplight_candidate.first_name = one_politician_array['first_name']
                maplight_candidate.middle_name = one_politician_array['middle_name']
                maplight_candidate.last_name = one_politician_array['last_name']
                maplight_candidate.name_prefix = one_politician_array['name_prefix']
                maplight_candidate.name_suffix = one_politician_array['name_suffix']
                maplight_candidate.bio = one_politician_array['bio']
                maplight_candidate.party = one_politician_array['party']
                maplight_candidate.candidate_flags = one_politician_array['candidate_flags']
                if validate_maplight_date(one_politician_array['last_funding_update']):
                    maplight_candidate.last_funding_update = one_politician_array['last_funding_update']
                maplight_candidate.roster_name = one_politician_array['roster_name']
                maplight_candidate.photo = one_politician_array['photo']
                maplight_candidate.url = one_politician_array['url']

                maplight_candidate.save()
                print "Candidate {display_name} added".format(
                    display_name=maplight_candidate.display_name)

            except Exception as e:
                handle_record_not_saved_exception(e)

        # TODO: Now link the candidate to the contest


