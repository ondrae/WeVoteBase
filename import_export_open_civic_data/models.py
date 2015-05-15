# import_export_open_civic_data/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.db import models

# https://github.com/opencivicdata/python-opencivicdata-django
# There are models for the ocd data types


# Other Open Civic Data identifiers that refer to the same division -- for example, those that refer to other
# political divisions whose boundaries are defined to be coterminous with this one.
# For example, ocd-division/country:us/state:wy will include an alias of ocd-division/country:us/state:wy/cd:1,
# since Wyoming has only one Congressional district.
#
# Division Identifiers here:
# Master CSV files with ocd-division-ids
# https://github.com/opencivicdata/ocd-division-ids/tree/master/identifiers
# https://raw.githubusercontent.com/opencivicdata/ocd-division-ids/master/identifiers/country-us.csv
# id,name,sameAs,sameAsNote,validThrough,census_geoid,census_geoid_12,census_geoid_14,openstates_district,placeholder_id,sch_dist_stateid,state_id
# ocd-division/country:us,United States,,,,,,,,,,
# ocd-division/country:us/court_of_appeals:1,United States Court of Appeals for 1st Circuit,,,,,,,,,,
# ocd-division/country:us/court_of_appeals:1/district_court:maine,United States District Court for District of Maine,,,,,,,,,,
# TODO create importer and table to cache this data
### Pulling out geographic divisions
# country / state /
#   cd  # congressional district, uses census_geoid ex/ ocd-division/country:us/state:ca/cd:12
#   circuit_court
#   county
#       council_district
#       school_district
#       precinct
#   parish
#       council_district
#       school_district
#       precinct
#       ward
#           council_district
#           school_district
#           precinct
#   place  - uses census_geoid
#   sldl  # State legislature district, lower
#   sldu  # State legislature district, upper
# country / territory /
#   municipio
#   sldl  # State legislature district, lower
#   sldu  # State legislature district, upper

