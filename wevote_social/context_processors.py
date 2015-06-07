"""Social template context processors"""

from facebook import FacebookAPI

def profile_photo(request):
    context_extras = {}
    if hasattr(request.user, 'social_auth'):
        facebook = FacebookAPI(request.user.social_auth)
        context_extras['profile_photo'] = facebook.profile_url()

    return context_extras
