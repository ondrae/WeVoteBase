# import_export_theunitedstatesio/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.import, name='import_states_from_api'),
    url(r'^(?P<pk>[A-Z]+)/$', views.StateDetailView.as_view(), name='statedetailview'),
]
