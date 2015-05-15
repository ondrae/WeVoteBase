# wevote_functions/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.db import models


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
