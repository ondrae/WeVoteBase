# ux_oak/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.shortcuts import render

from politician.models import Politician
from election_office_measure.models import BallotItemCache
from position.models import PositionListForCandidateCampaign


def my_ballot_view(request):
    ballot_item_list = BallotItemCache.objects.order_by('ballot_item_label')

    template_values = {
        'ballot_item_list':                         ballot_item_list,
    }
    return render(request, 'ux_oak/my_ballot.html', template_values)
