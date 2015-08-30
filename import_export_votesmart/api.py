# import_export_votesmart/api.py
# Brought to you by We Vote. Be good.
# https://github.com/votinginfoproject
# -*- coding: UTF-8 -*-

import requests


VOTESMART_API_URL = "http://api.votesmart.org"
VOTESMART_API_KEY = "b9fcf5c176722fc12b09d7a941e21f3e"


def get_api_route(cls, method):
    """Return full URI."""
    return "{url}/{cls}.{method}".format(
        url=VOTESMART_API_URL,
        cls=cls,
        method=method
    )

def make_request(cls, method, **kwargs):
    kwargs['key'] = VOTESMART_API_KEY
    if not kwargs.get('o'):
        kwargs['o'] = "JSON"
    url = get_api_route(cls, method)
    resp = requests.get(url, params=kwargs)
    if resp.status_code == 200:
        return resp.json()
    else:
        return resp.text
