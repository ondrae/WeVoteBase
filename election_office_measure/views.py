# election_office_measure/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.shortcuts import render


def my_ballot_view(request):
    politician_list = Politician.objects.order_by('last_name')
    template_values = {
        'politician_list': politician_list,
    }
    return render(request, 'ux_birch/start.html', template_values)  # Could be ux_oak too
