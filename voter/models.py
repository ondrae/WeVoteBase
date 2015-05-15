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


## Turned off AUTH_USER_MODEL in wevoteprojectbase/settings.py
# class VoterManager(BaseUserManager):
#
#     def _create_voter(self, email, password,
#                      is_staff, is_superuser, **extra_fields):
#         """
#         Creates and saves a User with the given email and password.
#         """
#         now = timezone.now()
#         if not email:
#             raise ValueError('The given email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email,
#                           is_staff=is_staff, is_active=True,
#                           is_superuser=is_superuser, last_login=now,
#                           date_joined=now, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_voter(self, email, password=None, **extra_fields):
#         return self._create_voter(email, password, False, False,
#                                  **extra_fields)
#
#     def create_superuser(self, email, password, **extra_fields):
#         return self._create_voter(email, password, True, True,
#                                  **extra_fields)
#
#
# class Voter(AbstractBaseUser, PermissionsMixin):
#     """
#     A fully featured User model with admin-compliant permissions that uses
#     a full-length email field as the username.
#
#     Email and password are required. Other fields are optional.
#     """
#     alphanumeric = RegexValidator(r'^[0-9a-zA-Z]*$', message='Only alphanumeric characters are allowed.')
#
#     # Redefine the basic fields that would normally be defined in User
#     username = models.CharField(unique=True, max_length=20, validators=[alphanumeric])  # Increase max_length to 255
#     email = models.EmailField(verbose_name='email address', max_length=254, unique=True)
#     first_name = models.CharField(verbose_name='first name', max_length=255, null=True, blank=True)
#     last_name = models.CharField(verbose_name='last name', max_length=255, null=True, blank=True)
#     date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
#     is_active = models.BooleanField(default=True, null=False)
#     is_admin = models.BooleanField(default=False, null=False)
#
#     # Custom We Vote fields
#     middle_name = models.CharField(max_length=255, null=True, blank=True)
# #     image_displayed
# #     image_twitter
# #     image_facebook
# #     blocked
# #     flags (ex/ signed_in)
# #     password_hashed
# #     password_reset_key
# #     password_reset_request_time
# #     last_activity
#
#     objects = VoterManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['username']
#
#     def get_full_name(self):
#         return self.first_name+" "+self.last_name
#
#     def get_short_name(self):
#         return self.first_name
#
#     def __str__(self):              # __unicode__ on Python 2
#         return self.get_full_name(self)
#
#     def has_permission(self, permission, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     def has_module_permissions(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True
#
#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin
#
#
# class VoterJurisdictionLink(models.Model):
#     """
#     All of the jurisdictions the Voter is in
#     """
#     voter = models.ForeignKey(Voter, null=False, blank=False, verbose_name='voter')
#     jurisdiction = models.ForeignKey(Jurisdiction,
#                                      null=False, blank=False, verbose_name="jurisdiction this voter votes in")