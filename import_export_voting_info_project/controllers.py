# import_export_voting_info_project/controllers.py
# Brought to you by We Vote. Be good.
# https://github.com/votinginfoproject
# -*- coding: UTF-8 -*-

from wevotebase.base import get_environment_variable
import wevote_functions.admin
import xmltodict


VOTING_INFO_PROJECT_SAMPLE_XML_FILE = get_environment_variable("VOTING_INFO_PROJECT_SAMPLE_XML_FILE")


logger = wevote_functions.admin.get_logger(__name__)


def import_voting_info_project_from_xml():
    logger.info("TO BE IMPLEMENTED")
    load_from_url = False
    if load_from_url:
        # Request json file from Google servers
        logger.info("Loading Sample XML from url")
        # request = requests.get(VOTER_INFO_URL, params={
        #     "key": GOOGLE_CIVIC_API_KEY,  # This comes from an environment variable
        #     "address": "254 Hartford Street San Francisco CA",
        #     "electionId": "2000",
        # })
        # structured_json = json.loads(request.text)
    else:
        # Load saved json from local file
        logger.info("Loading sample XML from local file")

        with open(VOTING_INFO_PROJECT_SAMPLE_XML_FILE) as xml_data:
            xml_in_dict_format = xmltodict.parse(xml_data)
        logger.info("Done")
