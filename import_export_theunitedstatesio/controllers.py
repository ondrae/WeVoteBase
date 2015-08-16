# import_export_theunitedstatesio/controllers.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from exception.models import handle_exception, handle_record_not_found_exception
import csv
from .models import LEGISLATORS_CURRENT_CSV_FILE, logger, TheUnitedStatesIoLegislatorCurrent


def import_legislators_current_csv():
    """
    This is a very simple method that is hard coded to the UnitedStates.io CSV Field names. We are saving
    the contents of this file locally so we can
    1) share the data on ElectionDataSummary.org dynamically
    2) save it/merge it into the correct We Vote tables later
    :return:
    """
    with open(LEGISLATORS_CURRENT_CSV_FILE, 'rU') as legislators_current_data:
        legislators_current_data.readline()             # Skip the header
        reader = csv.reader(legislators_current_data)   # Create a regular tuple reader
        for index, legislator_row in enumerate(reader):
            # if index > 7:
            #     break
            logger.debug("import_legislators_current_csv: " + legislator_row[0])  # For debugging
            legislator_entry_found = False

            # Do we have a record of this legislator based on bioguide_id?
            if legislator_row[18] != "":
                try:
                    query1 = TheUnitedStatesIoLegislatorCurrent.objects.all()
                    query1 = query1.filter(bioguide_id__exact=legislator_row[18])

                    # Was at least one existing entry found based on the above criteria?
                    if len(query1):
                        legislator_entry = query1[0]
                        legislator_entry_found = True
                except Exception as e:
                    handle_record_not_found_exception(e, logger=logger)

            if not legislator_entry_found:
                # TheUnitedStatesIoLegislatorCurrent was not found based on bioguide id
                # ...so check to see if we have a record of this legislator based on govtrack id?
                if legislator_row[23] != "":
                    try:
                        query2 = TheUnitedStatesIoLegislatorCurrent.objects.all()
                        query2 = query2.filter(govtrack_id__exact=legislator_row[23])

                        # Was at least one existing entry found based on the above criteria?
                        if len(query2):
                            legislator_entry = query2[0]
                            legislator_entry_found = True
                    except Exception as e:
                        handle_record_not_found_exception(e, logger=logger)

            if not legislator_entry_found:
                # TheUnitedStatesIoLegislatorCurrent was not found based on govtrack id
                # ...so create a new entry
                legislator_entry = TheUnitedStatesIoLegislatorCurrent(
                    last_name=legislator_row[0],                          # "last_name",               # row[0]
                    first_name=legislator_row[1],                         # "first_name",               # row[1]
                )

            legislator_entry.last_name = legislator_row[0]              # "last_name",              # row[0]
            legislator_entry.first_name = legislator_row[1]             # "first_name",             # row[1]
            legislator_entry.birth_date = legislator_row[2]             # "birthday",               # row[2]
            legislator_entry.gender = legislator_row[3]                 # "gender",                 # row[3]
            # "type",                   # row[4]
            legislator_entry.state = legislator_row[5]                  # "state",                  # row[5]
            # "district",               # row[6]  # Convert this to ocd district
            legislator_entry.party = legislator_row[7]                  # "party",                  # row[7]
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
            legislator_entry.bioguide_id = legislator_row[18]           # "bioguide_id",            # row[18]
            legislator_entry.thomas_id = legislator_row[19]             # "thomas_id",              # row[19]
            legislator_entry.opensecrets_id = legislator_row[20]        # "opensecrets_id",         # row[20]
            legislator_entry.lis_id = legislator_row[21]                # "lis_id",                 # row[21]
            legislator_entry.cspan_id = legislator_row[22]              # "cspan_id",               # row[22]
            legislator_entry.govtrack_id = legislator_row[23]           # "govtrack_id",            # row[23]
            legislator_entry.votesmart_id = legislator_row[24]          # "votesmart_id",           # row[24]
            legislator_entry.ballotpedia_id = legislator_row[25]        # "ballotpedia_id",         # row[25]
            legislator_entry.washington_post_id = legislator_row[26]    # "washington_post_id",     # row[26]
            legislator_entry.icpsr_id = legislator_row[27]              # "icpsr_id",               # row[27]
            legislator_entry.wikipedia_id = legislator_row[28]          # "wikipedia_id"            # row[28]

            # Add "try/exception" so we know when entry isn't saved due to unique requirement
            try:
                legislator_entry.save()
            except Exception as e:
                handle_exception(e, logger=logger)
