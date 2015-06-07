import urllib2
import logging
import json

logger = logging.getLogger()

class FacebookAPI(object):
    """API to Facebook's opengraph."""

    def __init__(self, social_auth):
        self.social_user = social_auth.filter(
            provider='facebook',
        ).first()
        print self.social_user

    def fetch_friends(self):
        request = self._request()
        friends = []

        try:
            friends = json.loads(urllib2.urlopen(request).read()).get('data')
        except Exception, err:
            logger.error(err)

        return friends

    def _request(self, **params):
        url = u'https://graph.facebook.com/{0}/' \
              u'friends?fields=id,name,location,picture' \
              u'&access_token={1}'.format(
                  self.social_user.uid,
                  self.social_user.extra_data['access_token'],
              )

        request = urllib2.Request(url)
        return request
