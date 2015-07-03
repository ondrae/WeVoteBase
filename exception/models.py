# exception/models.py
# Brought to you by We Vote. Be good.
# -*- coding: UTF-8 -*-

import inspect
import wevote_functions.admin


default_logger = wevote_functions.admin.get_logger(__name__)


def handle_exception(e, logger=None):
    if not logger:
        logger = default_logger

    exception_message = ""
    caller_frame_record = inspect.stack()[1]
    frame = caller_frame_record[0]
    info = inspect.getframeinfo(frame)

    logger.error(e)
    logger.error("{message}file: {filename}, line: {line}, function: {function}".format(
        message=exception_message,
        filename=info.filename,
        function=info.function,
        line=info.lineno
    ))


def handle_exception_silently(e):
    nothing = e  # Here for formatting only


def handle_record_not_deleted_exception(e, logger=None):
    if not logger:
        logger = default_logger

    exception_message = "Database record not deleted "
    caller_frame_record = inspect.stack()[1]
    frame = caller_frame_record[0]
    info = inspect.getframeinfo(frame)

    logger.error(e)
    logger.error("{message}file: {filename}, line: {line}, function: {function}".format(
        message=exception_message,
        filename=info.filename,
        function=info.function,
        line=info.lineno
    ))


def handle_record_not_found_exception(e, logger=None):
    if not logger:
        logger = default_logger

    exception_message = "Database record not found "
    caller_frame_record = inspect.stack()[1]
    frame = caller_frame_record[0]
    info = inspect.getframeinfo(frame)

    logger.error(e)
    logger.error("{message}file: {filename}, line: {line}, function: {function}".format(
        message=exception_message,
        filename=info.filename,
        function=info.function,
        line=info.lineno
    ))


def handle_record_found_more_than_one_exception(e, logger=None):
    if not logger:
        logger = default_logger

    exception_message = "More than one Database record found - only one expected "
    caller_frame_record = inspect.stack()[1]
    frame = caller_frame_record[0]
    info = inspect.getframeinfo(frame)

    logger.error(e)
    logger.error("{message}file: {filename}, line: {line}, function: {function}".format(
        message=exception_message,
        filename=info.filename,
        function=info.function,
        line=info.lineno
    ))


def handle_record_not_saved_exception(e, logger=None):
    if not logger:
        logger = default_logger

    exception_message = "Could not save "
    caller_frame_record = inspect.stack()[1]
    frame = caller_frame_record[0]
    info = inspect.getframeinfo(frame)

    logger.error(e)
    logger.error("{message}file: {filename}, line: {line}, function: {function}".format(
        message=exception_message,
        filename=info.filename,
        function=info.function,
        line=info.lineno
    ))
