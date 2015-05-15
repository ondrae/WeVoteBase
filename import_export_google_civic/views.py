# import_export_google_civic/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from import_export_google_civic.models import import_voterinfo_from_json


def import_voterinfo_from_json_view(request):
    """
    Take data from google civic information URL (JSON format) and store in the local database (???)
    Then display the data retrieved again from the local database
    """
    save_to_db = True
    json_from_google = import_voterinfo_from_json(save_to_db)

    template_values = {
        # 'legislator_list': TheUnitedStatesIoLegislatorCurrent.objects.order_by('last_name')[:25],
        'json_from_google': json_from_google,
    }
    return render(request, 'import_export_google_civic/import_voterinfo_from_json.html', template_values)
