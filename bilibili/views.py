from django.http import HttpResponse, QueryDict
from django.shortcuts import render, redirect

from bilibili.models import User


def index(request):
    return render(request, "bilibili/index.html")


def login(request):
    return render(request, "bilibili/login.html", {"title": "Welcome to login","path": "/login"})


def register(request):
    if request.method == 'POST':
        # Get all the request content
        data = request.body
        # get email, username and password field from request
        input_email = QueryDict(data).__getitem__("email")
        input_username = QueryDict(data).__getitem__("username")
        input_password = QueryDict(data).__getitem__("password")
        # insert to database
        User.objects.create(username=input_username, email=input_email, password=input_password)
        return redirect("backstage/")
    else:
        return render(request, "bilibili/register.html", {"title": "Welcome to register","path": "/register"})


def backstage(request):
    return render(request, "bilibili/backstage.html")
