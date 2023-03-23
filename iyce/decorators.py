from functools import wraps
from django.contrib import messages
from django.contrib.auth.views import redirect_to_login
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.contrib.auth.decorators import user_passes_test

from django.shortcuts import resolve_url
from urllib.parse import urlparse

import iyce.settings as settings
import requests


default_message = 'Unauthorised action.'


def superuser_required(view_func=None, redirect_field_name=REDIRECT_FIELD_NAME, login_url='/login', message=default_message):

    """
    Decorator for views that checks the user is login and is a superuser
    """

    actual_decorator = user_passes_test(
        lambda u: u.is_active and u.is_superuser and u.is_authenticated,
        login_url=login_url,
        redirect_field_name=redirect_field_name,
    
    )

    if view_func:
        return actual_decorator(view_func)
    return actual_decorator    