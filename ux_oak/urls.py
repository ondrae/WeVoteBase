# ux_oak/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from ux_oak import views

urlpatterns = [
    url(r'^$', views.my_ballot_view, name='my_ballot'),
    # url(r'^new_process/$', views.tag_new_process_view, name='tag_new_process'),
]
