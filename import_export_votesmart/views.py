# import_export_theunitedstatesio/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.shortcuts import redirect, render
from django.views import generic

from .models import State
from .controllers import load_states


def import_states_from_api(request):
    """
    """
    # If person isn't signed in, we don't want to let them visit this page yet
    if not request.user.is_authenticated():
        return redirect('/admin')

    load_states()

    template_values = {
        'state': State.objects.order_by('name'),
    }
    return render(request, 'import_export_votesmart/import.html', template_values)


class StateDetailView(generic.DetailView):
    model = State
    template_name = 'templates/statedetailview.html'

    def get_context_data(self):
        return State.objects
