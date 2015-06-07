# import_export_maplight/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.contrib import messages
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from import_export_maplight.models import import_maplight_from_json_view

def import_maplight_from_json_view(request):
    """
    Take data from Test XML file and store in the local Voting Info Project database
    """
    # If person isn't signed in, we don't want to let them visit this page yet
    if not request.user.is_authenticated():
        return redirect('/admin')

    import_maplight_from_json_sample_files()

    messages.add_message(request, messages.INFO, 'Maplight sample data imported.')

    return HttpResponseRedirect(reverse('import_export:import_export_index', args=()))
