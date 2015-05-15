# import_export/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.shortcuts import render

from politician.models import Politician
from import_export.models import transfer_google_civic_voterinfo_cached_data_to_wevote_tables, \
    transfer_theunitedstatesio_cached_data_to_wevote_tables


# http://localhost:8000/import_export/
def import_export_index(request):
    """
    Provide an index of import/export actions (for We Vote data maintenance)
    """

    template_values = {

    }
    return render(request, 'import_export/index.html', template_values)


# http://localhost:8000/import_export/transfer_from_google_civic/
def import_export_transfer_google_civic_to_local_tables_view(request):
    """
    Take data from the local TheUnitedStatesIo database (TheUnitedStatesIoLegislatorCurrent)
    and transfer it to the We Vote data structures
    """
    transfer_google_civic_voterinfo_cached_data_to_wevote_tables()

    template_values = {
        'politician_list': Politician.objects.order_by('last_name'),
    }
    return render(request, 'import_export/transfer_from_google_civic.html', template_values)


# http://localhost:8000/import_export/transfer_from_theunitedstatesio
def import_export_transfer_theunitedstatesio_to_local_tables_view(request):
    """
    Take data from the local TheUnitedStatesIo database (TheUnitedStatesIoLegislatorCurrent)
    and transfer it to the We Vote data structures
    """
    transfer_theunitedstatesio_cached_data_to_wevote_tables()

    template_values = {
        'politician_list': Politician.objects.order_by('last_name'),
    }
    return render(request, 'import_export/transfer_from_theunitedstatesio.html', template_values)