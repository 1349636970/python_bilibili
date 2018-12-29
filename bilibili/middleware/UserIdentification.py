import re

from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect


class UserLoginRequest:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        url_list = []
        for url in settings.NOT_REQUEST_LOGIN_URL:
            url_list.append(re.compile(url.lstrip('/')))
        response = self.get_response(request)
        if not request.user.is_authenticated:
            if not any(url.match(request.path_info.lstrip('/')) for url in url_list):
                return redirect('/login/')
            else:
                return response
        else:
            return response
