# import_export/urls.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.import_export_index, name='import_export_index'),
    url(r'^transfer_from_google_civic/', views.import_export_transfer_google_civic_to_local_tables_view,
        name='transfer_from_google_civic'),
    url(r'^transfer_from_theunitedstatesio/', views.import_export_transfer_theunitedstatesio_to_local_tables_view,
        name='transfer_from_theunitedstatesio'),
]