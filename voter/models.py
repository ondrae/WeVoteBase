# voter/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.core.validators import RegexValidator
from django.utils import timezone
from region_jurisdiction.models import Jurisdiction

# This way of extending the base user described here:
# https://docs.djangoproject.com/en/1.8/topics/auth/customizing/#a-full-example
# I then altered with this: http://buildthis.com/customizing-djangos-default-user-model/


# class VoterTwitterLink(models.Model):
#     voter_id
#     twitter_handle
#     confirmed_signin_date


# See AUTH_USER_MODEL in wevotebase/settings.py
class VoterManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        now = timezone.now()
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(email, password=password)
        user.is_admin = True
        user.save(using=self._db)
        return user

#     def retrieve_voter_from_voter_device_id(self, voter_device_id):
#         print "retrieve_voter_from_cookie"
#         voter_device_id_manager = VoterDeviceIdManager()
#         voter_id = voter_device_id_manager.retrieve_voter_id_from_voter_device_id(voter_device_id)
#
#         if not voter_id:
#             results = {
#                 'voter_found':  False,
#                 'voter_id':     0,
#                 'voter':        Voter(),
#             }
#             return results
#
#         voter_manager = VoterManager()
#         results = voter_manager.retrieve_voter_by_id(voter_id)
#         if results['voter_found']:
#             voter = results['voter']
#
#         voter_on_stage_found = voter
#         results = {
#             'voter_found':  False,
#             'voter_id':     0,
#             'voter':        Voter(),
#         }
#         return voter
#
#
# class VoterDeviceIdManager():
#
#     def retrieve_voter_id_from_voter_device_id(self, voter_device_id):
#         voter_manager = VoterManager()
#         voter_manager.
#         return voter_id

class Voter(AbstractBaseUser):
    """
    A fully featured User model with admin-compliant permissions that uses
    a full-length email field as the username.

    Email and password are required. Other fields are optional.
    """
    alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')

    # Redefine the basic fields that would normally be defined in User
    # username = models.CharField(unique=True, max_length=20, validators=[alphanumeric])  # Increase max_length to 255
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    first_name = models.CharField(verbose_name='first name', max_length=255, null=True, blank=True)
    last_name = models.CharField(verbose_name='last name', max_length=255, null=True, blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # Custom We Vote fields
    middle_name = models.CharField(max_length=255, null=True, blank=True)
#     image_displayed
#     image_twitter
#     image_facebook
#     blocked
#     flags (ex/ signed_in)
#     password_hashed
#     password_reset_key
#     password_reset_request_time
#     last_activity

    objects = VoterManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  # Since we need to store a voter based solely on voter_device_id, no values are required

    def get_full_name(self):
        # return self.first_name+" "+self.last_name
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # return self.first_name
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        # return self.get_full_name(self)
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


# class VoterJurisdictionLink(models.Model):
#     """
#     All of the jurisdictions the Voter is in
#     """
#     voter = models.ForeignKey(Voter, null=False, blank=False, verbose_name='voter')
#     jurisdiction = models.ForeignKey(Jurisdiction,
#                                      null=False, blank=False, verbose_name="jurisdiction this voter votes in")