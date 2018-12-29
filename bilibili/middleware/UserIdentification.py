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
        path = request.path_info.lstrip('/')
        results = []
        for url in url_list:
            results.append(url.match(path))
        """if not request.user.is_authenticated:
            if not any(result):
                return redirect('/login/')
            else:
                return response
        else:
            return response
            """
        return HttpResponse(any(result for result in results))
