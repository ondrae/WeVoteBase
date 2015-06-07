# import_export_maplight/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.import_maplight_from_json_view, name='import_maplight_from_json_view'),
]
