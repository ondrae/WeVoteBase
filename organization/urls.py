# organization/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<organization_id>[0-9]+)/edit/$', views.organization_edit_view, name='organization_edit'),
    url(r'^edit_process/$', views.organization_edit_process_view, name='organization_edit_process'),
    url(r'^$', views.organization_list_view, name='organization_list',),
    url(r'^edit/$', views.organization_new_view, name='organization_new'),
    url(r'^(?P<organization_id>[0-9]+)/pos/$', views.organization_position_list_view,
        name='organization_position_list',),
    url(r'^(?P<organization_id>[0-9]+)/pos/(?P<position_id>[0-9]+)/$', views.organization_position_edit_view,
        name='organization_position_edit',),
    url(r'^(?P<organization_id>[0-9]+)/pos/new/$', views.organization_position_new_view,
        name='organization_position_new',),
    url(r'^pos/edit_process/$', views.organization_position_edit_process_view,
        name='organization_position_edit_process'),
]