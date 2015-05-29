# ux_oak/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.shortcuts import render
from election_office_measure.models import BallotItemCache
from wevote_functions.models import get_voter_device_id, set_voter_device_id


def my_ballot_view(request):
    voter_device_id = get_voter_device_id(request, True)

    ballot_item_list = BallotItemCache.objects.order_by('ballot_item_label')

    template_values = {
        'ballot_item_list':                         ballot_item_list,
    }
    response = render(request, 'ux_oak/my_ballot.html', template_values)

    set_voter_device_id(request, response, voter_device_id)
    return response

def start_view(request):
    ballot_item_list = BallotItemCache.objects.order_by('ballot_item_label')
    template_values = {
        'ballot_item_list': ballot_item_list,
    }
    return render(request, 'ux_oak/start.html', template_values)
