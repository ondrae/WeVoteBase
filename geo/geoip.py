"""
"""
import os
from pygeoip import GeoIP, GeoIPError

from django.conf import settings

_GEOIP_INSTANCE = None

def getInstance():
    """Retuns the singleton instance of GeoIP"""
    global _GEOIP_INSTANCE
    if _GEOIP_INSTANCE:
        return _GEOIP_INSTANCE

    geoipdb_path = os.path.join(settings.GEOIP_PATH, settings.GEOIP_CITY)
    _GEOIP_INSTANCE = GeoIP(geoipdb_path)
    return _GEOIP_INSTANCE
