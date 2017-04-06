from datetime import datetime
from flask import flash, request, url_for
import arrow

def flash_errors(form, category='danger'):
    for field, errors in form.errors.items():
        for error in errors:
            flash(
                u'%s - %s' % (getattr(form, field).label.text, error),
                category
            )


def url_for_other_page(remove_args=[], **kwargs):
    args = request.args.copy()
    remove_args = ['_pjax']
    for key in remove_args:
        if key in args.keys():
            args.pop(key)
    new_args = [x for x in kwargs.items()]
    for key, value in new_args:
        args[key] = value
    return url_for(request.endpoint, **args)


def timeago(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a pretty string
    like 'an hour ago', 'Yesterday', '3 months ago', 'just now', etc
    """

    return arrow.get(time).humanize()


def format_date(time=False):
    """
    Get a datetime object or a int() Epoch timestamp and return a pretty string
    like 'an hour ago', 'Yesterday', '3 months ago', 'just now', etc
    """

    return arrow.get(time).format('DD-MM-YYYY')
