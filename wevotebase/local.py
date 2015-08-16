# wevotebase/local.py (Local Settings)
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': get_environment_variable('DATABASE_ENGINE'),
        'NAME': get_environment_variable('DATABASE_NAME'),
        'USER': get_environment_variable('DATABASE_USER'),
        'PASSWORD': get_environment_variable('DATABASE_PASSWORD'),
        'HOST': get_environment_variable('DATABASE_HOST'),  # localhost
        'PORT': get_environment_variable('DATABASE_PORT'),  # 5432
    }
}

# ########## Logging configurations ###########
#   LOG_STREAM          Boolean     True will turn on stream handler and write to command line.
#   LOG_FILE            String      Path to file to write to. Make sure executing
#                                   user has permissions.
#   LOG_STREAM_LEVEL    Integer     Log level of stream handler: CRITICAL, ERROR, INFO, WARN, DEBUG
#   LOG_FILE_LEVEL      Integer     Log level of file handler: CRITICAL, ERROR, INFO, WARN, DEBUG
LOG_STREAM = True
LOG_FILE = get_environment_variable('LOG_FILE')
LOG_STREAM_LEVEL = logging.DEBUG
LOG_FILE_LEVEL = logging.ERROR
