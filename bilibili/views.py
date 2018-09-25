from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader


def index(request):
    template = loader.get_template('index.html')
    content = {}
    return HttpResponse(template.render(content, request))


def login(request):
    template = loader.get_template('login.html')
    content = {}
    return HttpResponse(template.render(content, request))
