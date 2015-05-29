# wevote_functions/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

import datetime, string, random


# Create your models here.
class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        """Return the match method once, then stop"""
        yield self.match
        raise StopIteration

    def match(self, *args):
        """Indicate whether or not to enter a case suite"""
        if self.fall or not args:
            return True
        elif self.value in args: # changed for v1.5, see below
            self.fall = True
            return True
        else:
            return False

# # Empty suites are considered syntax errors, so intentional fall-throughs
# # should contain 'pass'
# c = 'z'
# for case in switch(c):
#     if case('a'): pass # only necessary if the rest of the suite is empty
#     if case('b'): pass
#     # ...
#     if case('y'): pass
#     if case('z'):
#         print "c is lowercase!"
#         break
#     if case('A'): pass
#     # ...
#     if case('Z'):
#         print "c is uppercase!"
#         break
#     if case(): # default
#         print "I dunno what c was!"

def convert_to_int(value):
    try:
        new_value = int(value)
    except ValueError:
        new_value = 0
    return new_value

# http://stackoverflow.com/questions/1622793/django-cookies-how-can-i-set-them
def set_cookie(response, cookie_name, cookie_value, days_expire=None):
    if days_expire is None:
        max_age = 10 * 365 * 24 * 60 * 60  # ten years
    else:
        max_age = days_expire * 24 * 60 * 60
    expires = datetime.datetime.strftime(datetime.datetime.utcnow() + datetime.timedelta(seconds=max_age),
                                         "%a, %d-%b-%Y %H:%M:%S GMT")
    response.set_cookie(cookie_name, cookie_value, max_age=max_age, expires=expires)

def get_voter_device_id(request, generate_if_no_cookie=False):
    voter_device_id = ''
    if 'voter_device_id' in request.COOKIES:
        voter_device_id = request.COOKIES['voter_device_id']
        # print "from cookie, voter_device_id: {voter_device_id}".format(voter_device_id=voter_device_id)
    if voter_device_id == '' and generate_if_no_cookie:
        voter_device_id = random_string_generator()  # Stored in cookie below
        # If we set this here, we won't know whether we need to store the cookie in set_voter_device_id
        # request.COOKIES['voter_device_id'] = voter_device_id  # Set it here for use in the remainder of this page load
        # print "random_string_generator, voter_device_id: {voter_device_id}".format(voter_device_id=voter_device_id)
    return voter_device_id

def set_voter_device_id(request, response, voter_device_id):
    if 'voter_device_id' not in request.COOKIES:
        set_cookie(response, 'voter_device_id', voter_device_id)

def random_string_generator(string_length=88, chars=string.ascii_lowercase + string.ascii_uppercase + string.digits):
    """
    Generate a random string.
    :param string_length:
    :param chars:
    :return:
    """
    return ''.join(random.SystemRandom().choice(chars) for _ in range(string_length))

