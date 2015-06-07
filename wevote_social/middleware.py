"""Social middleware"""

from facebook import FacebookAPI

class SocialMiddleware(object):
    def process_request(self, request):
        if request.user and hasattr(request.user, 'social_auth'):
            # Assume facebook for now
            request.facebook = FacebookAPI(request.user.social_auth)

        return None
