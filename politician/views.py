# politician/views.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.contrib import messages
from django.contrib.messages import get_messages
from django.core.urlresolvers import reverse
from django.views import generic
from django.views.generic import TemplateView
from django.utils import timezone

from .forms import TagNewForm
from .models import Politician, PoliticianTagLink
from tag.models import Tag


class PoliticianIndexView(generic.ListView):
    template_name = 'politician/politician_list.html'
    context_object_name = 'politician_list'

    def get_queryset(self):
        """"""
        return Politician.objects.order_by('last_name')


# TODO Next step is to get Twitter vacuum working so we can pull in Tweets automatically based on tags/handles
def politician_detail_view(request, politician_id):
    politician_on_stage = get_object_or_404(Politician, id=politician_id)
    # post_list = Post.objects.filter
    template_values = {
        'politician_on_stage': politician_on_stage,
        # 'post_list': tag_list,  # This is for prototyping only -- we want to move very quickly to posts being pulled onto the page via javascript
    }
    return render(request, 'politician/politician_detail.html', template_values)


def politician_tag_new_view(request, politician_id):
    """
    Form to add a new link tying a politician to twitter tags
    :param request:
    :return:
    """
    messages_on_stage = get_messages(request)
    # for message in messages_on_stage:
    #     if message.level is ERROR:

    politician_on_stage = get_object_or_404(Politician, id=politician_id)

    try:
        tag_link_list = politician_on_stage.tag_link.all()
    except PoliticianTagLink.DoesNotExist:
        tag_link_list = None
    template_values = {
        'politician_on_stage': politician_on_stage,
        'tag_link_list': tag_link_list,
        'messages_on_stage': messages_on_stage,
    }
    return render(request, 'politician/politician_tag_new.html', template_values)


def politician_tag_new_test_view(request, politician_id):
    """
    Form to add a new link tying a politician to twitter tags
    :param request:
    :return:
    """
    tag_new_form = TagNewForm()
    politician_on_stage = get_object_or_404(Politician, id=politician_id)
    # TODO Find the tags attached to this politician
    try:
        tag_list = PoliticianTagLink.objects.get(politician=politician_on_stage)
    except PoliticianTagLink.DoesNotExist:
        tag_list = None
    template_values = {
        'tag_new_form': tag_new_form,
        'politician_on_stage': politician_on_stage,
        'tag_list': tag_list,
    }
    return render(request, 'politician/politician_tag_new_test.html', template_values)


def politician_tag_new_process_view(request, politician_id):
    """
    Process the form to add a new link tying a politician to twitter tags
    """
    politician_on_stage = get_object_or_404(Politician, id=politician_id)
    new_tag = request.POST['new_tag']

    # If an invalid tag didn't come in, redirect back to tag_new
    if not is_tag_valid(new_tag):
        messages.add_message(request, messages.INFO, 'That is not a valid tag. Please enter a different tag.')
        return HttpResponseRedirect(reverse('politician:politician_tag_new', args=(politician_id,)))

    new_tag_temp, created = Tag.objects.get_or_create(hashtag_text=new_tag)
    new_tag_link = PoliticianTagLink(tag=new_tag_temp, politician=politician_on_stage)
    new_tag_link.save()

    return HttpResponseRedirect(reverse('politician:politician_detail', args=(politician_id,)))


def is_tag_valid(new_tag):
    if not bool(new_tag.strip()):  # If this doesn't evaluate true here, then it is empty and isn't valid
        return False
    return True
