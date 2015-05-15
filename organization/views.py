# organization/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.contrib.messages import get_messages
from django.shortcuts import render
from exception.models import handle_exception, handle_exception_silently, handle_record_found_more_than_one_exception,\
    handle_record_not_found_exception, handle_record_not_saved_exception

from election_office_measure.models import CandidateCampaign, MeasureCampaign
from organization.models import Organization
from position.models import Position, PositionEntered


def organization_list_view(request):
    messages_on_stage = get_messages(request)
    organization_list = Organization.objects.order_by('name')

    template_values = {
        'messages_on_stage': messages_on_stage,
        'organization_list': organization_list,
    }
    return render(request, 'organization/organization_list.html', template_values)


def organization_new_view(request):
    messages_on_stage = get_messages(request)
    template_values = {
        'messages_on_stage': messages_on_stage,
    }
    return render(request, 'organization/organization_edit.html', template_values)


def organization_edit_view(request, organization_id):
    messages_on_stage = get_messages(request)
    organization_on_stage_found = False
    try:
        organization_on_stage = Organization.objects.get(id=organization_id)
        organization_on_stage_found = True
    except Organization.MultipleObjectsReturned as e:
        handle_record_found_more_than_one_exception(e)
    except Organization.DoesNotExist as e:
        # This is fine, create new
        handle_exception_silently(e)

    if organization_on_stage_found:
        template_values = {
            'messages_on_stage': messages_on_stage,
            'organization': organization_on_stage,
        }
    else:
        template_values = {
            'messages_on_stage': messages_on_stage,
        }
    return render(request, 'organization/organization_edit.html', template_values)


def organization_edit_process_view(request):
    organization_id = request.POST['organization_id']
    organization_name = request.POST['organization_name']

    # Check to see if this organization is already being used anywhere
    organization_on_stage_found = False
    try:
        # organization_query = Organization.objects.all()
        # organization_query = organization_query.filter(id=organization_id)
        organization_query = Organization.objects.filter(id=organization_id)
        if len(organization_query):
            organization_on_stage = organization_query[0]
            organization_on_stage_found = True
    except Exception as e:
        handle_record_not_found_exception(e)

    try:
        if organization_on_stage_found:
            # Update
            organization_on_stage.name = organization_name
            organization_on_stage.save()
            messages.add_message(request, messages.INFO, 'Organization updated.')
        else:
            # Create new
            organization_on_stage = Organization(
                name=organization_name,
            )
            organization_on_stage.save()
            messages.add_message(request, messages.INFO, 'New organization saved.')
    except Exception as e:
        handle_record_not_saved_exception(e)
        messages.add_message(request, messages.ERROR, 'Could not save organization.')

    return HttpResponseRedirect(reverse('organization:organization_list', args=()))


def organization_position_list_view(request, organization_id):
    messages_on_stage = get_messages(request)

    organization_on_stage_found = False
    try:
        organization_query = Organization.objects.filter(id=organization_id)
        if len(organization_query):
            organization_on_stage = organization_query[0]
            organization_on_stage_found = True
    except Exception as e:
        handle_record_not_found_exception(e)
        organization_on_stage_found = False

    if not organization_on_stage_found:
        messages.add_message(request, messages.ERROR,
                             'Could not find organization when trying to retrieve positions.')
        return HttpResponseRedirect(reverse('organization:organization_list', args=()))
    else:
        organization_position_list_found = False
        try:
            organization_position_list = PositionEntered.objects.order_by('stance')
            organization_position_list = organization_position_list.filter(organization_id=organization_id)
            if len(organization_position_list):
                organization_position_list_found = True
        except Exception as e:
            handle_record_not_found_exception(e)

        if organization_position_list_found:
            template_values = {
                'messages_on_stage': messages_on_stage,
                'organization': organization_on_stage,
                'organization_position_list': organization_position_list,
            }
        else:
            template_values = {
                'messages_on_stage': messages_on_stage,
                'organization': organization_on_stage,
            }
    return render(request, 'organization/organization_position_list.html', template_values)


def organization_position_new_view(request, organization_id):
    messages_on_stage = get_messages(request)
    organization_on_stage_found = False
    try:
        organization_on_stage = Organization.objects.get(id=organization_id)
        organization_on_stage_found = True
    except Organization.MultipleObjectsReturned as e:
        handle_record_found_more_than_one_exception(e)
    except Organization.DoesNotExist as e:
        # This is fine, create new
        handle_exception_silently(e)

    if not organization_on_stage_found:
        messages.add_message(request, messages.INFO,
                             'Could not find organization when trying to create a new position.')
        return HttpResponseRedirect(reverse('organization:organization_position_list', args=([organization_id])))
    else:
        template_values = {
            'messages_on_stage': messages_on_stage,
            'organization': organization_on_stage,
        }
    return render(request, 'organization/organization_position_edit.html', template_values)


def organization_position_edit_view(request, organization_id, position_id):
    messages_on_stage = get_messages(request)
    organization_on_stage_found = False
    try:
        organization_on_stage = Organization.objects.get(id=organization_id)
        organization_on_stage_found = True
    except Organization.MultipleObjectsReturned as e:
        handle_record_found_more_than_one_exception(e)
    except Organization.DoesNotExist as e:
        # This is fine, create new
        handle_exception_silently(e)

    if not organization_on_stage_found:
        messages.add_message(request, messages.INFO,
                             'Could not find organization when trying to edit a position.')
        return HttpResponseRedirect(reverse('organization:organization_position_list', args=([organization_id])))

    # Get the existing position
    organization_position_on_stage_found = False
    try:
        organization_position_on_stage = PositionEntered.objects.get(id=position_id)
        organization_position_on_stage_found = True
    except Organization.MultipleObjectsReturned as e:
        handle_record_found_more_than_one_exception(e)
    except Organization.DoesNotExist as e:
        # This is fine, create new
        handle_exception_silently(e)

    if organization_position_on_stage_found:
        template_values = {
            'messages_on_stage': messages_on_stage,
            'organization': organization_on_stage,
            'organization_position': organization_position_on_stage,
        }
    else:
        messages.add_message(request, messages.INFO,
                             'Could not find organization position when trying to edit.')
        return HttpResponseRedirect(reverse('organization:organization_position_list', args=([organization_id])))
    return render(request, 'organization/organization_position_edit.html', template_values)


def organization_position_edit_process_view(request):
    organization_id = request.POST['organization_id']
    position_id = request.POST['position_id']
    candidate_campaign_id = request.POST['candidate_campaign_id']
    measure_campaign_id = request.POST['measure_campaign_id']

    # Check to see if this organization is already being used anywhere
    organization_on_stage_found = False
    try:
        organization_query = Organization.objects.filter(id=organization_id)
        if len(organization_query):
            organization_on_stage = organization_query[0]
            organization_on_stage_found = True
    except Exception as e:
        # If we can't retrieve the organization, we cannot proceed
        handle_record_not_found_exception(e)
        messages.add_message(
            request, messages.ERROR,
            "Could not find the organization when trying to create or edit a new position.")
        return HttpResponseRedirect(reverse('organization:organization_list', args=()))

    # Now retrieve the CandidateCampaign or the MeasureCampaign so we can save it with the Position
    if candidate_campaign_id:
        try:
            candidate_campaign_on_stage = CandidateCampaign.objects.get(id=candidate_campaign_id)
            candidate_campaign_on_stage_found = True
        except CandidateCampaign.MultipleObjectsReturned as e:
            handle_record_found_more_than_one_exception(e)
        except CandidateCampaign.DoesNotExist as e:
            handle_record_not_found_exception(e)
            messages.add_message(
                request, messages.ERROR,
                "Could not find Candidate's campaign when trying to create or edit a new position.")
            if position_id:
                return HttpResponseRedirect(
                    reverse('organization:organization_position_edit', args=([organization_id]))
                )
            else:
                return HttpResponseRedirect(
                    reverse('organization:organization_position_new', args=([organization_id]))
                )
        # Retrieve position if it exists already
        organization_position_found = False
        if position_id:
            print "Retrieve existing position"

        # Now save
        try:
            if organization_position_found:
                # Update
                print "Update organization_position"
            else:
                # Create new
                organization_position_on_stage = PositionEntered(
                    organization_id=organization_id,
                    candidate_campaign=candidate_campaign_on_stage,
                )
                organization_position_on_stage.save()
                messages.add_message(
                    request, messages.INFO,
                    "New position saved.")
        except Exception as e:
            handle_record_not_saved_exception(e)
            print "Problem saving PositionEntered for CandidateCampaign"

    elif measure_campaign_id:
        print "Look for MeasureCampaign here"

    # Create a new PositionEntered
    # try:
    #     if organization_on_stage_found:
    #         # Update
    #         organization_on_stage.name = organization_name
    #         organization_on_stage.save()
    #         messages.add_message(request, messages.INFO, 'Organization updated.')
    #     else:
    #         # Create new
    #         organization_on_stage = Organization(
    #             name=organization_name,
    #         )
    #         organization_on_stage.save()
    #         messages.add_message(request, messages.INFO, 'New organization saved.')
    # except Exception as e:
    #     handle_record_not_saved_exception(e)
    #     messages.add_message(request, messages.ERROR, 'Could not save organization.')

    return HttpResponseRedirect(reverse('organization:organization_position_list', args=([organization_id])))
