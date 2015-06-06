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
    url(r'^position_json/', views.ExportPositionDataToJson, name='position_json'),
    url(r'^candidate_campaigns/', views.ExportCandidateCampaignDataToJson.as_view()),
    url(r'^organizations/', views.ExportOrganizationDataToJson.as_view()),
    url(r'^positions/', views.ExportPositionDataToJson.as_view()),
    url(r'^update_all_id_we_vote/', views.update_all_id_we_vote, name='update_all_id_we_vote'),
    url(r'^import_sample_positions/', views.import_we_vote_sample_positions_data_from_json,
        name='import_sample_positions'),
]
