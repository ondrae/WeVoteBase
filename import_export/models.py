# import_export/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.db import models
from exception.models import handle_exception, handle_record_not_found_exception, handle_record_not_saved_exception
from politician.models import Politician
from election_office_measure.models import Election, ContestOffice, CandidateCampaign, ContestMeasure, \
    MeasureCampaign, BallotItemCache
from import_export_theunitedstatesio.models import import_legislators_current_csv, TheUnitedStatesIoLegislatorCurrent
from import_export_google_civic.models import GoogleCivicElection, GoogleCivicContestOffice, \
    GoogleCivicCandidateCampaign, GoogleCivicContestReferendum


def import_politician_data_from_theunitedstatesio():
    """
    In this method, we import TheUnitedStates.io source data to a local table cache, and then take the cached
    data and move it/merge it with core We Vote data
    :return:
    """
    import_legislators_current_csv()
    transfer_theunitedstatesio_cached_data_to_wevote_tables()


def transfer_theunitedstatesio_cached_data_to_wevote_tables():
    """
    In this method, we take the cached theunitedstatesio data and move it into the core We Vote data
    :return:
    """
    print "Running transfer_theunitedstatesio_cached_data_to_wevote_tables()"

    legislators_current_query = TheUnitedStatesIoLegislatorCurrent.objects.all()
    # Only retrieve entries that haven't been processed yet
    # legislators_current_query = legislators_current_query.filter(was_processed=False)

    for legislator_current_entry in legislators_current_query:
        print 'Transferring: ' + str(legislator_current_entry.id) + ':' \
              + legislator_current_entry.first_name + ' ' + legislator_current_entry.last_name
        politician_entry_found = False

        #########################
        # Search the Politician's table to see if we already have an entry for this person
        # Do we have a record of this politician based on id_bioguide?
        if legislator_current_entry.bioguide_id != "":
            try:
                # Try to find earlier version based on the bioguide identifier
                query1 = Politician.objects.all()
                query1 = query1.filter(id_bioguide__exact=legislator_current_entry.bioguide_id)

                # Was at least one existing entry found based on the above criteria?
                if len(query1):
                    politician_entry = query1[0]
                    politician_entry_found = True
            except Exception as e:
                handle_record_not_found_exception(e)

        if not politician_entry_found:
            # TheUnitedStatesIoLegislatorCurrent was not found based on bioguide id
            # ...so check to see if we have a record of this legislator based on govtrack id?
            if legislator_current_entry.govtrack_id != "":
                try:
                    query1 = Politician.objects.all()
                    query1 = query1.filter(id_govtrack__exact=legislator_current_entry.govtrack_id)

                    # Was at least one existing entry found based on the above criteria?
                    if len(query1):
                        politician_entry = query1[0]
                        print "FOUND"
                        politician_entry_found = True
                    else:
                        print "NOT FOUND"
                except Exception as e:
                    handle_record_not_found_exception(e)

        if not politician_entry_found:
            # TheUnitedStatesIoLegislatorCurrent was not found based on id_govtrack
            # ...so check to see if we have a record of this legislator based on full_name_google_civic
            if legislator_current_entry.first_name and legislator_current_entry.last_name:
                try:
                    full_name_assembled_guess = legislator_current_entry.first_name+" "+legislator_current_entry.last_name
                    print "Searching for existing full_name_google_civic: {full_name_assembled}".format(
                        full_name_assembled=full_name_assembled_guess)
                    query1 = Politician.objects.all()
                    query1 = query1.filter(full_name_google_civic=full_name_assembled_guess)

                    # Was at least one existing entry found based on the above criteria?
                    if len(query1):
                        politician_entry = query1[0]
                        print "FOUND"
                        politician_entry_found = True
                    else:
                        print "NOT FOUND"
                except Exception as e:
                    handle_record_not_found_exception(e)

        if not politician_entry_found:
            # TheUnitedStatesIoLegislatorCurrent was not found based on full_name_google_civic
            # ...so check to see if we have a record of this legislator based on full_name_assembled
            if legislator_current_entry.first_name and legislator_current_entry.last_name:
                try:
                    full_name_assembled_guess = legislator_current_entry.first_name+" "+legislator_current_entry.last_name
                    print "Searching for existing full_name_assembled: {full_name_assembled}".format(
                        full_name_assembled=full_name_assembled_guess)
                    query1 = Politician.objects.all()
                    query1 = query1.filter(full_name_assembled=full_name_assembled_guess)

                    # Was at least one existing entry found based on the above criteria?
                    if len(query1):
                        politician_entry = query1[0]
                        print "FOUND"
                        politician_entry_found = True
                    else:
                        print "NOT FOUND"
                except Exception as e:
                    handle_record_not_found_exception(e)

        if not politician_entry_found:
            # TheUnitedStatesIoLegislatorCurrent was not found
            # ...so create a new entry
            politician_entry = Politician(
                last_name=legislator_current_entry.last_name,
                first_name=legislator_current_entry.first_name,
                full_name_assembled=legislator_current_entry.first_name+" "+legislator_current_entry.last_name,
            )

        politician_entry.last_name = legislator_current_entry.last_name
        politician_entry.first_name = legislator_current_entry.first_name
        politician_entry.full_name_assembled = \
            legislator_current_entry.first_name+" "+legislator_current_entry.last_name
        politician_entry.birth_date = legislator_current_entry.birthday
        politician_entry.gender = legislator_current_entry.gender
        politician_entry.id_bioguide = legislator_current_entry.bioguide_id
        politician_entry.id_thomas = legislator_current_entry.thomas_id
        politician_entry.id_opensecrets = legislator_current_entry.opensecrets_id
        politician_entry.id_lis = legislator_current_entry.lis_id
        politician_entry.id_cspan = legislator_current_entry.cspan_id
        politician_entry.id_govtrack = legislator_current_entry.govtrack_id
        politician_entry.id_votesmart = legislator_current_entry.votesmart_id
        politician_entry.id_ballotpedia = legislator_current_entry.ballotpedia_id
        politician_entry.id_washington_post = legislator_current_entry.washington_post_id
        politician_entry.id_icpsr = legislator_current_entry.icpsr_id
        politician_entry.id_wikipedia = legislator_current_entry.wikipedia_id


        # OTHER FIELDS
        # "type",                   # row[4]
        politician_entry.state_code = legislator_current_entry.state                # "state",  # row[5]
        # "district",               # row[6]
        politician_entry.party = legislator_current_entry.party                     # "party",  # row[7]
        # "url",                    # row[8]
        # "address",                # row[9]
        # "phone",                  # row[10]
        # "contact_form",           # row[11]
        # "rss_url",                # row[12]
        # "twitter",                # row[13]
        # "facebook",               # row[14]
        # "facebook_id",            # row[15]
        # "youtube",                # row[16]
        # "youtube_id",             # row[17]

        # We use "try/exception" so we know when entry isn't saved due to unique requirement
        # This works! Bigger question -- how to deal with exceptions in general?
        try:
            politician_entry.save()
            # Mark the source entry as was_processed so we don't try to import the same data again
            # legislator_current_entry.save()
        except Exception as e:
            handle_exception(e)


def transfer_google_civic_voterinfo_cached_data_to_wevote_tables():
    """
    In this method, we take the cached google civic data and move it into the core We Vote data with some grooming
    :return:
    """
    print "Running transfer_google_civic_voterinfo_cached_data_to_wevote_tables()"

    # Capture election information
    google_civic_save_election()

    # Politician linking
    google_civic_link_politician_to_campaign()

    # CandidateCampaign

    # ContestMeasure

    # MeasureCampaign

    # Populate BallotItemCache


def google_civic_save_election():
    # Bring in the GoogleCivicElection and save the Election
    google_civic_query1 = GoogleCivicElection.objects.all()
    # Only retrieve entries that haven't been processed yet
    # google_civic_query1 = google_civic_query1.filter(was_processed=False)

    for google_civic_election_entry in google_civic_query1:
        election_exists_locally = False

        #########################
        # Search the Election table to see if we already have an entry for this election
        if google_civic_election_entry.google_civic_election_id != "":
            try:
                # Try to find earlier version based on the google_civic_election_id identifier
                query1 = Election.objects.all()
                query1 = query1.filter(
                    google_civic_election_id__exact=google_civic_election_entry.google_civic_election_id)

                # Was at least one existing entry found based on the above criteria?
                if len(query1):
                    election_entry = query1[0]
                    election_exists_locally = True
            except Exception as e:
                handle_record_not_found_exception(e)
                continue

        try:
            if election_exists_locally:
                # Update the values
                election_entry.google_civic_election_id = google_civic_election_entry.google_civic_election_id
                election_entry.name = google_civic_election_entry.name+"TEST"
                election_entry.election_date_text = google_civic_election_entry.election_day
            else:
                # An entry in the local Election was not found based on google_civic_election_id
                # ...so create a new entry
                election_entry = Election(
                    google_civic_election_id=google_civic_election_entry.google_civic_election_id,
                    name=google_civic_election_entry.name,
                    election_date_text=google_civic_election_entry.election_day,
                )

            election_entry.save()

            # Mark the source entry as was_processed so we don't try to import the same data again
            # google_civic_election_entry.was_processed = True

            # Save the local we vote id back to the imported google civic data for cross-checking
            google_civic_election_entry.we_vote_election_id = election_entry.id
            google_civic_election_entry.save()

        except Exception as e:
            handle_record_not_saved_exception(e)
            continue
    # END OF google_civic_save_election


def google_civic_link_politician_to_campaign():

    # Bring in the GoogleCivicCandidateCampaign and save the CandidateCampaign
    google_civic_candidate_campaign_query = GoogleCivicCandidateCampaign.objects.all()

    for google_civic_candidate_campaign_entry in google_civic_candidate_campaign_query:

        if not google_civic_candidate_campaign_entry.google_civic_election_id:
            print "We cannot proceed with {name} -- there is no google_civic_election_id".format(
                name=google_civic_candidate_campaign_entry.name)
            continue

        try:
            election_query = Election.objects.all()
            election_query = election_query.filter(
                google_civic_election_id=google_civic_candidate_campaign_entry.google_civic_election_id)

            if len(election_query) == 1:
                election_on_stage = election_query[0]
            else:
                print "ERROR: Break out of main loop without an election_on_stage -- single Election entry not found"
                continue
        except Exception as e:
            handle_record_not_found_exception(e)
            continue

        ###########################################
        # Election
        # The election is linked below

        ###########################################
        # ContestOffice
        # We want to find or create a We Vote ContestOffice
        results = google_civic_get_or_create_contest_office(google_civic_candidate_campaign_entry, election_on_stage)
        try:
            contest_office_error = results['error_result']
            if contest_office_error:
                print "ERROR returned in google_civic_get_or_create_contest_office "\
                      "(skipping to next google_civic_candidate_campaign_entry)"
                continue
            contest_office_on_stage = results['contest_office_on_stage']
            contest_office_created = results['contest_office_created']

            # Link this ContestOffice to the Election that was created above
            contest_office_on_stage.election_id = election_on_stage.id
            contest_office_on_stage.save()  # We save here AND lower in case there are failures
        except Exception as e:
            handle_record_not_saved_exception(e)
            continue

        ###########################################
        # CandidateCampaign
        # We want to find or create a We Vote CandidateCampaign
        results = google_civic_get_or_create_candidate_campaign_basic(google_civic_candidate_campaign_entry)
        candidate_campaign_error = results['error_result']
        if candidate_campaign_error:
            print "ERROR returned in google_civic_get_or_create_candidate_campaign_basic "\
                  "(skipping to next google_civic_candidate_campaign_entry)"
            continue
        politician_link_needed = results['politician_link_needed']
        candidate_campaign_created = results['candidate_campaign_created']
        candidate_campaign_on_stage = results['candidate_campaign_on_stage']

        try:
            # Add/update campaign information
            candidate_campaign_on_stage.candidate_name = google_civic_candidate_campaign_entry.name
            candidate_campaign_on_stage.party = google_civic_candidate_campaign_entry.party

            # Link this CandidateCampaign to the Election and ContestOffice that was created above
            candidate_campaign_on_stage.election_id = election_on_stage.id
            candidate_campaign_on_stage.google_civic_election_id = \
                google_civic_candidate_campaign_entry.google_civic_election_id
            candidate_campaign_on_stage.contest_office_id = contest_office_on_stage.id
            candidate_campaign_on_stage.save()

            # We want to save the local id back to the GoogleCivicCandidateCampaign table
            # so we can cross-check data-integrity
            # NOTE: We do not limit this linkage to when we first create these local entries
            google_civic_candidate_campaign_entry.we_vote_election_id = election_on_stage.id
            google_civic_candidate_campaign_entry.we_vote_contest_office_id = contest_office_on_stage.id
            google_civic_candidate_campaign_entry.we_vote_candidate_campaign_id = candidate_campaign_on_stage.id
            google_civic_candidate_campaign_entry.save()  # We save here AND lower in case there are failures
        except Exception as e:
            handle_record_not_saved_exception(e)
            continue

        ###########################################
        # Politician
        # We know that a politician is not currently linked to this campaign
        # if politician_link_needed:  # DALE 2015-05-03 I would like this to always refresh
        results = google_civic_get_or_create_politician(google_civic_candidate_campaign_entry)
        politician_error = results['error_result']
        if politician_error:
            print "ERROR returned in google_civic_get_or_create_politician "\
                  "(skipping to next google_civic_candidate_campaign_entry)"
            continue
        politician_on_stage = results['politician_on_stage']

        try:
            candidate_campaign_on_stage.politician_id = politician_on_stage.id
            candidate_campaign_on_stage.save()

            google_civic_candidate_campaign_entry.we_vote_politician_id = politician_on_stage.id
            google_civic_candidate_campaign_entry.save()
        except Exception as e:
            handle_record_not_saved_exception(e)
            continue
    # END OF google_civic_link_politician_to_campaign


def google_civic_get_or_create_contest_office(google_civic_candidate_campaign_entry, election_on_stage):
    error_result = False
    ballot_item_on_stage_found = False
    try:
        # When we import from google, we link a google_civic_contest_office entry (with an internal id) to
        #  google_civic_candidate_campaign_entry
        # print "Retrieving google_civic_contest_office"
        google_civic_contest_office_query = GoogleCivicContestOffice.objects.all()
        google_civic_contest_office_query = google_civic_contest_office_query.filter(id=google_civic_candidate_campaign_entry.google_civic_contest_office_id)

        if len(google_civic_contest_office_query) == 1:
            google_civic_contest_office_on_stage = google_civic_contest_office_query[0]
        else:
            print "Single google_civic_contest_office NOT found"
            return {
                'error_result': True,
            }

        # Try to find earlier version based on the google_civic_election_id identifier
        # print "Retrieving contest_office"
        contest_office_query = ContestOffice.objects.all()
        contest_office_query = contest_office_query.filter(google_civic_election_id=google_civic_contest_office_on_stage.google_civic_election_id)
        contest_office_query = contest_office_query.filter(district_name=google_civic_contest_office_on_stage.district_name)
        contest_office_query = contest_office_query.filter(office_name=google_civic_contest_office_on_stage.office)
        # TODO: If the 'office' text from Google Civic changes slightly, we would create a new ContestOffice entry
        # (which would not be correct) Should we make this more robust and error-proof?

        # Was at least one existing entry found based on the above criteria?
        if len(contest_office_query):
            contest_office_on_stage = contest_office_query[0]
            contest_office_created = False

            # TODO Update contest_office information here
        elif len(contest_office_query) > 1:
            # We have bad data - a duplicate
            print "We have bad data, a duplicate ContestOffice entry: {office}".format(office=google_civic_contest_office_on_stage.office)
            return {
                'error_result': True,
            }
        else:
            # Create a new ContestOffice entry
            # print "Creating contest_office"
            contest_office_on_stage = ContestOffice(
                office_name=google_civic_contest_office_on_stage.office,
                election_id=election_on_stage.id,
                google_civic_election_id=google_civic_contest_office_on_stage.google_civic_election_id,
                number_voting_for=google_civic_contest_office_on_stage.number_voting_for,
                number_elected=google_civic_contest_office_on_stage.number_elected,
                primary_party=google_civic_contest_office_on_stage.primary_party,
                district_name=google_civic_contest_office_on_stage.district_name,
                district_scope=google_civic_contest_office_on_stage.district_scope,
                district_ocd_id=google_civic_contest_office_on_stage.district_ocd_id,
            )
            contest_office_on_stage.save()
            contest_office_created = True

        google_civic_contest_office_on_stage.we_vote_election_id = election_on_stage.id
        google_civic_contest_office_on_stage.we_vote_contest_office_id = contest_office_on_stage.id
        google_civic_contest_office_on_stage.save()

        # Save the ballot_placement
        # Try to find earlier version based on the google_civic_election_id identifier
        # print "Retrieving BallotItemCache"
        ballot_item_query = BallotItemCache.objects.all()
        ballot_item_query = ballot_item_query.filter(voter_id=1)
        ballot_item_query = ballot_item_query.filter(google_civic_election_id=google_civic_contest_office_on_stage.google_civic_election_id)
        ballot_item_query = ballot_item_query.filter(contest_office_id=contest_office_on_stage.id)
        if len(ballot_item_query) == 1:
            ballot_item_on_stage = ballot_item_query[0]
            ballot_item_on_stage_found = True
    except Exception as e:
        error_result = True
        handle_record_not_found_exception(e)

    try:
        if ballot_item_on_stage_found:
            # Update the values
            ballot_item_on_stage.election_id = election_on_stage.id
            # TODO Add all values here
        else:
            # print "Creating BallotItemCache"
            ballot_item_on_stage = BallotItemCache(
                voter_id=1,
                election_id=election_on_stage.id,
                google_civic_election_id=google_civic_contest_office_on_stage.google_civic_election_id,
                contest_office_id=contest_office_on_stage.id,
                # contest_measure_id: Used for measures/referendum/initiatives
                ballot_order=google_civic_contest_office_on_stage.ballot_placement,
                ballot_item_label=google_civic_contest_office_on_stage.office,
            )
        ballot_item_on_stage.save()
    except Exception as e:
        error_result = True
        handle_record_not_saved_exception(e)

    results = {
        'error_result': error_result,
        'contest_office_on_stage': contest_office_on_stage,
        'contest_office_created': contest_office_created,
    }
    return results
    # END OF google_civic_get_or_create_contest_office


def google_civic_get_or_create_candidate_campaign_basic(google_civic_candidate_campaign_entry):
    """
    Search the CandidateCampaign table to see if we already have an entry for this election
    :param google_civic_candidate_campaign_entry:
    :return:
    """
    error_result = False
    candidate_campaign_exists_locally = False
    candidate_campaign_created = False
    politician_link_needed = True
    try:
        # Try to find earlier version based on the google_civic_election_id identifier
        candidate_campaign_query = CandidateCampaign.objects.all()
        candidate_campaign_query = candidate_campaign_query.filter(google_civic_election_id__exact=google_civic_candidate_campaign_entry.google_civic_election_id)
        # TODO: If the name from Google Civic changes slightly, we would create a new campaign entry
        # (which would not be correct) We should make this more robust and error-proof
        candidate_campaign_query = candidate_campaign_query.filter(candidate_name__exact=google_civic_candidate_campaign_entry.name)

        # Was at least one existing entry found based on the above criteria?
        if len(candidate_campaign_query):
            candidate_campaign_on_stage = candidate_campaign_query[0]
            candidate_campaign_exists_locally = True
            # Is a Politician linked to this candidate_campaign_on_stage
            if candidate_campaign_on_stage.politician_id:
                politician_link_needed = False
    except Exception as e:
        error_result = True
        handle_record_not_found_exception(e)

    if not candidate_campaign_exists_locally:
        # An entry in the local CandidateCampaign table was not found
        # ...so create a new entry
        try:
            candidate_campaign_on_stage = CandidateCampaign(
                google_civic_election_id=google_civic_candidate_campaign_entry.google_civic_election_id,
                candidate_name=google_civic_candidate_campaign_entry.name,
                party=google_civic_candidate_campaign_entry.party,
            )
            candidate_campaign_on_stage.save()
            candidate_campaign_created = True
        except Exception as e:
            error_result = True
            handle_record_not_saved_exception(e)

    results = {
        'error_result': error_result,
        'politician_link_needed': politician_link_needed,
        'candidate_campaign_created': candidate_campaign_created,
        'candidate_campaign_on_stage': candidate_campaign_on_stage,
    }

    return results
    # END OF google_civic_get_or_create_candidate_campaign_basic


def google_civic_get_or_create_politician(google_civic_candidate_campaign_entry):
    error_result = False
    ##########################
    # Does this politician exist locally?
    politician_on_stage_found = False
    first_name_guess = google_civic_candidate_campaign_entry.name.partition(' ')[0]
    last_name_guess = google_civic_candidate_campaign_entry.name.partition(' ')[-1]
    try:
        # print "We are searching based on full_name_google_civic"
        query1 = Politician.objects.all()
        query1 = query1.filter(full_name_google_civic=google_civic_candidate_campaign_entry.name)

        # Was at least one existing entry found based on the above criteria?
        if len(query1):
            politician_on_stage = query1[0]
            politician_on_stage_found = True
            if len(query1) > 1:
                # We have confusion, so skip processing this google_civic_candidate_campaign_entry
                print "More than one Politician found (query1)"
        else:
            print "No politician found based on full_name_google_civic: {name}".format(
                name=google_civic_candidate_campaign_entry.name)
    except Exception as e:
        handle_record_not_found_exception(e)

    if not politician_on_stage_found:
        # No entries were found, so we need to
        # a) Search more deeply
        # Searching based on full_name_assembled
        print "Searching against full_name_assembled: {name}".format(name=google_civic_candidate_campaign_entry.name)
        # TODO DALE 2015-05-02 With this code, if we had imported a "Betty T. Yee" from another non-google-civic
        #  source (where full_name_google_civic was empty), we would create a second Politician entry. Fix this.
        try:
            politician_query_full_name_assembled = Politician.objects.all()
            politician_query_full_name_assembled = politician_query_full_name_assembled.filter(
                full_name_assembled=google_civic_candidate_campaign_entry.name)

            if len(politician_query_full_name_assembled):
                politician_on_stage = politician_query_full_name_assembled[0]
                politician_on_stage_found = True
            else:
                print "No politician found based on full_name_assembled: {name}".format(
                    name=google_civic_candidate_campaign_entry.name)
        except Exception as e:
            handle_record_not_found_exception(e)

    if not politician_on_stage_found:
        # No entries were found, so we need to
        # a) Search more deeply
        print "first_name_guess: {first_name_guess}, last_name_guess: {last_name_guess}".format(first_name_guess=first_name_guess, last_name_guess=last_name_guess)
        # TODO DALE 2015-05-02 With this code, if we had imported a "Betty T. Yee" from another non-google-civic
        #  source (where full_name_google_civic was empty), we would create a second Politician entry. Fix this.
        try:
            politician_query_first_last_guess = Politician.objects.all()
            politician_query_first_last_guess = politician_query_first_last_guess.filter(first_name=first_name_guess)
            politician_query_first_last_guess = politician_query_first_last_guess.filter(last_name=last_name_guess)

            if len(politician_query_first_last_guess):
                politician_on_stage = politician_query_first_last_guess[0]
                politician_on_stage_found = True
            else:
                print "No politician found based on first_name_guess: {first_name} and last_name_guess: {last_name}".format(
                    first_name=first_name_guess,
                    last_name=last_name_guess)
        except Exception as e:
            handle_record_not_found_exception(e)

    try:
        if politician_on_stage_found:
            # We found a match, and want to update the Politician data to match how Google Civic references the name
            # print "Store google_civic_candidate_campaign_entry.name in Politician.full_name_google_civic"
            politician_on_stage.full_name_google_civic = google_civic_candidate_campaign_entry.name
        else:
            # print "Create Politician entry: {name}".format(name=google_civic_candidate_campaign_entry.name)
            politician_on_stage = Politician(
                # Do not save first_name or last_name because middle initials will throw this off
                last_name=last_name_guess,
                first_name=first_name_guess,
                full_name_google_civic=google_civic_candidate_campaign_entry.name,
            )
        politician_on_stage.save()
    except Exception as e:
        handle_record_not_saved_exception(e)

    if error_result:
        print "There was an error trying to create a politician"
    # else:
        # print "It seems we have found a politician: {display_full_name}".format(display_full_name=politician_on_stage.display_full_name())
        # print "It seems we have found a politician: "+str(politician_on_stage.display_full_name())
        # print "It seems we found or created a politician."

    results = {
        'error_result': error_result,
        'politician_on_stage': politician_on_stage,
    }
    return results
