# support_oppose_deciding/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.http import JsonResponse
from django.shortcuts import render
from position.models import PositionEnteredManager

def voter_supporting_candidate_campaign_view(request, candidate_campaign_id):
    print "voter_supporting_candidate_campaign_view {candidate_campaign_id}".format(
        candidate_campaign_id=candidate_campaign_id)
    voter_id = 1
    position_entered_manager = PositionEnteredManager()
    results = position_entered_manager.toggle_on_voter_support_for_candidate_campaign(voter_id, candidate_campaign_id)
    if results['success']:
        return JsonResponse({0: "success"})
    else:
        return JsonResponse({0: "failure"})


def voter_stop_supporting_candidate_campaign_view(request, candidate_campaign_id):
    print "voter_stop_supporting_candidate_campaign_view {candidate_campaign_id}".format(
        candidate_campaign_id=candidate_campaign_id)
    voter_id = 1
    position_entered_manager = PositionEnteredManager()
    results = position_entered_manager.toggle_off_voter_support_for_candidate_campaign(voter_id, candidate_campaign_id)
    if results['success']:
        return JsonResponse({0: "success"})
    else:
        return JsonResponse({0: "failure"})


def voter_opposing_candidate_campaign_view(request, candidate_campaign_id):
    print "voter_opposing_candidate_campaign_view {candidate_campaign_id}".format(
        candidate_campaign_id=candidate_campaign_id)
    voter_id = 1
    position_entered_manager = PositionEnteredManager()
    results = position_entered_manager.toggle_on_voter_oppose_for_candidate_campaign(voter_id, candidate_campaign_id)
    if results['success']:
        return JsonResponse({0: "success"})
    else:
        return JsonResponse({0: "failure"})


def voter_stop_opposing_candidate_campaign_view(request, candidate_campaign_id):
    print "voter_stop_opposing_candidate_campaign_view {candidate_campaign_id}".format(
        candidate_campaign_id=candidate_campaign_id)
    voter_id = 1
    position_entered_manager = PositionEnteredManager()
    results = position_entered_manager.toggle_off_voter_oppose_for_candidate_campaign(voter_id, candidate_campaign_id)
    if results['success']:
        return JsonResponse({0: "success"})
    else:
        return JsonResponse({0: "failure"})


def voter_asking_candidate_campaign_view(request, candidate_campaign_id):
    print "voter_asking_candidate_campaign_view {candidate_campaign_id}".format(
        candidate_campaign_id=candidate_campaign_id)
    return JsonResponse({0: "not working yet - needs to be built"})


def voter_stop_asking_candidate_campaign_view(request, candidate_campaign_id):
    print "voter_stop_asking_candidate_campaign_view {candidate_campaign_id}".format(
        candidate_campaign_id=candidate_campaign_id)
    return JsonResponse({0: "not working yet - needs to be built"})


def voter_stance_for_candidate_campaign_view(request, candidate_campaign_id):
    print "voter_stance_for_candidate_campaign_view {candidate_campaign_id}".format(
        candidate_campaign_id=candidate_campaign_id)
    voter_id = 1
    position_entered_manager = PositionEnteredManager()
    results = position_entered_manager.retrieve_voter_candidate_campaign_position(voter_id, candidate_campaign_id)
    if results['position_found']:
        if results['is_support']:
            return JsonResponse({0: "support"})
        elif results['is_oppose']:
            return JsonResponse({0: "oppose"})
        elif results['is_no_stance']:
            return JsonResponse({0: "no_stance"})
        elif results['is_information_only']:
            return JsonResponse({0: "information_only"})
        elif results['is_still_deciding']:
            return JsonResponse({0: "still_deciding"})
    return JsonResponse({0: "failure"})


def voter_stance_for_measure_campaign_view(request, measure_campaign_id):
    print "voter_stance_for_candidate_campaign_view {candidate_campaign_id}".format(
        measure_campaign_id=measure_campaign_id)
    return JsonResponse({0: "not working yet - needs to be built"})
