# import_export_azavea_cicero/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

import wevote_functions.admin

# from django.db import models


logger = wevote_functions.admin.get_logger(__name__)


# CiceroElectionEvent
# http://cicero.azavea.com/docs/election_event.html
# id  # The primary key for the current record.
# sk  # The surrogate key for the current record. For more information on using the surrogate key, read about historical queries.
# last_update_date  # Datetime string indicating when the record was last updated.
# valid_from  # Used in historical queries.
# valid_to  # Used in historical queries.
# label = None  # A short text label of the ElectionEvent
# election_date_text = None  # A textual representation of the election date or range of dates
# election_expire_date = None  # A datetime indicating the day on which the election ends. (e.g. "2008-11-04 00:00:00.000")
# is_approximate = None  # Boolean that is true if the election date is approximate.
# is_by_election = None  # Boolean that is true if the election is a by-election (also known as a special election)
# is_primary_election = None  # Boolean indicating that the ElectionEvent represents a primary election.
# is_runoff_election = None  # Boolean indicating that this is the second election round in a two-round voting system.
# is_referendum = None  # Boolean indicating whether or not the election includes a referendum on the ballot.
# is_local = None  # Boolean indicating that the ElectionEvent represents a local election
# is_state = None  # Boolean indicating that the ElectionEvent represents a state or provincial election
# is_national = None  # Boolean indicating that the ElectionEvent represents a national election
# is_transnational = None  # Boolean indicating that the ElectionEvent represents a transnational election

# CiceroDistrict
# http://cicero.azavea.com/docs/district.html
# id  # The primary key for the current record.
# sk  # The surrogate key for the current record. For more information on using the surrogate key, read about historical queries.
# last_update_date  # Datetime string indicating when the record was last updated.
# valid_from  # Used in historical queries.
# valid_to  # Used in historical queries.
# district_type  # The name_short value for the related district. See the DistrictType documentation page for more information.
# subtype = None  # A subset of district_type
#     CENSUS subtypes
#         PUMA (United States only)
#         URBAN_AREA (known as a metropolitan area in Canada)
#         COUNTY
#             In Canada: Census division, which may be a county, municipalite regionale de comte, regional district, or equivalent area defined by Statistics Canada
#             In the United States: county or statistically equivalent entity
#         TRACT
#         SUBDIVISION
#             In Australia: local government area
#             In the United States: county subdivision
#         PLACE (United States only)
#         BLOCK_GROUP (known as a dissemination area in Canada)
#     SCHOOL subtypes
#         ELEMENTARY
#         SECONDARY
#         UNIFIED
#     WATERSHED subtypes
#         HUC2 (U.S. only)
#         HUC4 (U.S. only)
#         HUC6 (U.S. only)
#         HUC8 (U.S. only)
#         WSC_MDA (Canada only)
#         WSC_SDA (Canada only)
#         WSC_SSDA (Canada only)
# district_id = None  # The District ID (usually a number) of the district, if applicable.
#     # The District ID is specific to the type of district. For example, it may indicate a police precinct,
#     # U.S. Census GEOID, or a city ward.
# city = None  # The local municipality that the District represents, if applicable.
# state = None  # The subnational geography (such as a state or province) that the District represents, coded using ISO 3166-2 suffix.
# country = None  # The country that the District represents (as a string), if applicable.
# label = None  # Text associated with a district_id, such as the position or group identifier for an at-large office,
#               # label for the district (e.g. "Ward"), or a full label for the district (e.g. "Sealaska Alaska Native
#               # Regional Corporation").


# DistrictType(id, name_short, name_long, notes, acknowledgements, is_legislative)
# http://cicero.azavea.com/docs/district_type.html
# name_short = None  # This field is used for district type lookups in other API calls.
# Possible values for legislative districts may include:
#     LOCAL (such as a city or a ward within a city)
#     LOCAL_2010 (redistricted based on the 2010 Census)
#     LOCAL_EXEC (such a city)
#     STATE_LOWER (such as a state assembly district)
#     STATE_LOWER_2010 (redistricted based on the 2010 Census)
#     STATE_UPPER (such as a state senate district)
#     STATE_UPPER_2010 (redistricted based on the 2010 Census)
#     STATE_EXEC (such as a province, territory, or state)
#     NATIONAL_LOWER (such as a member of Parliament)
#     NATIONAL_LOWER_2010 (redistricted based on the 2010 Census)
#     NATIONAL_UPPER (such as a member of the Lords)
#     NATIONAL_EXEC (such as a president or prime minister)
# Possible values for non-legislative districts may include:
#     CENSUS
#     COUNTY
#     JUDICIAL
#     POLICE
#     SCHOOL
#     WATERSHED
# name_long = None  # This is a longer description of the district type.
# is_legislative = None  # True if this is a legislative district (use the legislative_district call).
                            # False if this is a nonlegislative district (use the nonlegislative_district call).


# CiceroOfficial
# http://cicero.azavea.com/docs/official.html
# id  # The primary key for the current record.
# sk  # The surrogate key for the current record. For more information on using the surrogate key, read about historical queries.
# last_update_date  # Datetime string indicating when the record was last updated.
# valid_from  # Used in historical queries.
# valid_to  # Used in historical queries.
# addresses  # A list of address objects for the given official. For each attribute in the address, the default is an empty string. Each object contains:
# current_term_start_date  # The date when the official started his or her term that took place during the time this record is valid.
# term_end_date  # The date when the official's term ended or is scheduled to end.
# email_addresses  # A list of e-mail address strings for the official.
# urls  # A list of website addresses related to the official. These may include the official's official page, campaign website, or the website for the assembly that he or she belongs to.
# office  # A CiceroOffice object
# identifier  # A list of Identifier objects (the Id for this official in a different database, like Bioguide or Vote Smart)
# notes  # A list of notes about the official.
# party = None  # The Official's political party
# initial_term_start_date = None  # Time at which the Official's first term began. May represent a year, month, or specific day as indicated by initial_term_start_date_precision
# initial_term_start_date_precision = None
#                 # Uppercase letter indicating the precision of initial_term_start_date:
#                 #     D indicates the term starts on the given day.
#                 #     M indicates the term starts within the given month.
#                 #     Y indicates the term starts within the given year.
# valid_from_precision = None
#                 # Uppercase letter indicating the precision of current_term_start_date
#                 #     D indicates the term starts on the given day.
#                 #     M indicates the term starts within the given month.
#                 #     Y indicates the term starts within the given year.
# valid_to_precision = None
#                 # Uppercase letter indicating the precision of term_end_date
#                 #     D indicates the term ends on the given day.
#                 #     M indicates the term ends within the given month.
#                 #     Y indicates the term ends within the given year.
# first_name = None  # The Official's first name.
# middle_initial = None  # The Official's middle initial or name.
# last_name = None  # The Official's last name.
# name_suffix = None  # Abbreviations ("Esq."), letters ("M.D.") and/or generational suffixes ("Jr.", "IV") that follow the Official's name.
# nickname = None  # A familiar name used by an Official in place of or in addition to his or her proper name.
# photo_origin_url = None  # URL of the Official's photo
# notes = None  # Notes about the Official
# url_1 = None  # URL of a website related to this Official
# url_2 = None  # URL of a website related to this Official
# salutation = None  # An honorific used when addressing an Official (e.g. "The Honourable")
# web_form_url = None  # URL of a web-based form that can be used to contact the Official
# committees  # A list (array) of Committee objects representing one or more committees on which the Official serves. This information may not be up-to-date.


# CiceroAddress (an attribute of Official -- not available via own API)
# address_1
# address_2
# address_3
# city
# county
# state
# postal_code
# phone_1
# fax_1
# phone_2
# fax_2

# CiceroOffice  # An object with these attributes:
# chamber  #
# district  #
# election_rules  #
# id  #
# last_update_date  #
# notes  #
# representing_city  #
# representing_state  #
# sk  #
# title  #
# valid_from  #
# valid_to  #


# CiceroChamber
# http://cicero.azavea.com/docs/chamber.html
# country  # cicero.webservice.models.Country object
# district_type  #
# last_update_date  # Datetime string indicating when the record was last updated.
# id  # The primary key for the current record.
# sk  # The surrogate key for the current record. For more information on using the surrogate key, read about historical queries.
# last_update_date  # Datetime string indicating when the record was last updated.
# valid_from  # Used in historical queries.
# valid_to  # Used in historical queries.
# government  # The government that this Chamber is part of. (Link to CiceroGovernemnt?)
# name = None  # Common name for this Chamber (in English).
# name_formal = None  # Formal name for this Chamber (in English).
# name_native_language = None  # Name for this Chamber (in the native language).
# type = None  # The type of Chamber. Possible values are:
#             # LOWER
#             # UPPER
#             # EXEC
# has_geographic_representation = None  # Boolean value indicating if this Chamber is geographically represented in Cicero.
# url = None  # URL to the Chamber's website
# contact_phone = None  # The Chamber's telephone number
# contact_email = None  # The general e-mail address for this Chamber
# remarks = None  # Notes about this Chamber
# election_rules = None  # Information about this Chamber's election rules
# redistricting_rules = None  # Information about this Chamber's redistricting rules
# term_length = None  # The term length for an Official in this Chamber (string).
# term_limit = None  # Term limit (maximum number of terms)
# vacancy_rules = None  # Vacancy laws
# election_frequency = None  # How often elections are held for this Chamber (string)
# inauguration_rules = None  # Inauguration rules for this Chamber
# official_count = None  # Number of members in this Chamber
# notes = None  # Notes about this Chamber
# is_chamber_complete = None  # If true, full district information for this Chamber exists in Cicero.
# last_verification_date = None  # Datetime of when the record was last verified (e.g. "2011-09-02 19:30:59.000")


# CiceroIdentifier (unique Ids for a variety of other dbs)
# Returns information about identifiers associated with an official. See official for instructions on querying Cicero for officials.
# The default sorting order for Identifiers is by identifier_type ascending.
# is_staging = None  # is_staging is overwritten to make the default false
# identifier_type = None  # Possible identifier types include, but are not limited to:
#                 # The Center for Responsive Politics (CRP)
#                 # The Congressional Biographical Directory (BIOGUIDE)
#                 # Facebook (FACEBOOK)
#                 # The Federal Election Commission (FEC)
#                 # Flickr (FLICKR)
#                 # Google+ (GOOGLEPLUS)
#                 # GovTrack (GOVTRACK)
#                 # Picasa (PICASA)
#                 # Project Vote Smart (VOTESMART)
#                 # RSS Feeds (RSS)
#                 # Twitter (TWITTER)
#                 # YouTube (YOUTUBE)
# identifier_value = None  # An external identifier related to an Official



# CiceroCountry(id, sk, valid_from, valid_to, trans_from, trans_to, is_staging, fips, iso_2, iso_3, iso_3_numeric, gmi_3, name_short, name_long, name_short_iso, name_short_un, name_short_local, name_long_local, status)
# http://cicero.azavea.com/docs/country.html
# id  # The primary key for the current record.
# sk  # The surrogate key for the current record. For more information on using the surrogate key, read about historical queries.
# last_update_date  # Datetime string indicating when the record was last updated.
# valid_from  # Used in historical queries.
# valid_to  # Used in historical queries.
# fips = None  # Two-letter country code specified in U.S. Federal Information Processing Standard No. 10.
# iso_2 = None  # Two-letter country code specified in the ISO 3166-1 alpha-2 standard. It is the most commonly-used code in the ISO 3166-1 standard.
# iso_3 = None  # Three-letter country code specified in the ISO 3166-1 alpha-3 standard.
# iso_3_numeric = None  # Current three-digit country code specified in the ISO 3166-1 numeric standard. This code is developed and maintained by the United Nations Statistics Division.
# gmi_3 = None  # Three-letter Global Mapping International (GMI) country/territory code.
# name_short = None  # Short, common country name in English.
# name_long = None  # Long country name in English.
# name_short_iso = None  # Official country short name (in English) specified in the ISO-3166 standard.
# name_short_un = None  # UN short country name
# name_short_local = None  # Short, common country name in the local language.
# name_long_local = None  # Long country name in the local language.
# status = None  # Parent organization (e.g. "UN Member State") and/or state on which the given Country is dependent (e.g. "Oversea Deparment of France").


# CiceroGovernment
# http://cicero.azavea.com/docs/government.html
# name = None  # Name of the Government
# type = None  # Describes the level of Government. Possible values are:
#             # LOCAL
#             # STATE
#             # NATIONAL
#             # TRANSNATIONAL
# city = None  # Local place where the Government is located (e.g. "Barcelona", "Fairbanks North Star Borough")
# state = None  # State, province, territory, or district where the Government is located (e.g. "PA", "Baghdad Province").
# country  # Country object which this Government is part of.
# url = None  # Goverment's web address
# notes = None  # Notes about the Government.
# last_update_user = None  # Identifier for the last user that updated this record. This property is not included in the API response.
