"""
LocationMiddleware
from geo import geoip
"""

import geo.geoip
import wevote_functions.admin

logger = wevote_functions.admin.get_logger(__name__)


class LocationMiddleware:
    """Gets the client IP address and checks it against the GeoIP database"""
    def __init__(self):
        self.geoip = geo.geoip.getInstance()

    def process_request(self, request):
        client_ip = None
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(',')[0] # Get the first one from the list

        if not client_ip:
            client_ip = request.META.get('REMOTE_ADDR')

        if not client_ip:
            client_ip = request.META.get('HTTP_X_REAL_IP')

        if not client_ip:
            logger.debug('Could not determine client ip address.')
            return None

        request.location = self.geoip.record_by_addr(client_ip)
        if request.location:
            logger.debug("Got location.", **request.location)
        else:
            logger.debug("No location available.", client_ip=client_ip)
