# import_export_voting_info_project/models.py
# Brought to you by We Vote. Be good.
# https://github.com/votinginfoproject
# -*- coding: UTF-8 -*-

from django.db import models
import requests
import wevote_functions.admin


logger = wevote_functions.admin.get_logger(__name__)

# Add models here