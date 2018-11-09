import logging
import uuid

from django.contrib import auth
from django.contrib.auth import authenticate, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect

from bilibili import models
from bilibili.models import BilibiliUser


def index(request):
    return render(request, "bilibili/index.html")


def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/backstage/')
        else:

            return redirect('/login/')
    else:
        return render(request, "bilibili/login.html",
                      {"title": "Welcome to login", "path": "/login/", "type_page": "login"})


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        BilibiliUser.objects.create_user(username, email, password)
        return redirect('backstage/')
    else:
        return render(request, "bilibili/register.html",
                      {"title": "Welcome to register", "path": "/register", "type_page": "register"})


def backstage(request):
    if request.user.is_authenticated:
        return render(request, "bilibili/backstage.html")
    else:
        return redirect('/login')


def logout_view(request):
    logout(request)
    websiteURL = request.GET.get('website')
    return redirect(websiteURL)


def uploadvideos(request):
    if request.user.is_authenticated:
        return render(request, 'bilibili/uploadVideo.html',
                      {"title": "Welcome to Upload Video", "path": "/transfer/",
                       "type_page": "uploadvideos"})
    else:
        return redirect('/login')


def transfer_station(request):
    video_files = request.FILES.get('video')
    video_title = request.POST.get('VideoTitle')
    video_description = request.POST.get("VideoDescription")
    video_userid = request.POST.get("userID")
    video_uuid = str(uuid.uuid4())
    dir_bilibili_file = {'title': video_title, 'description': video_description, 'userId': video_userid,
                         'uuid': video_uuid, 'upload': video_files}
    models.BilibiliFile.objects.create(**dir_bilibili_file)
    return HttpResponse("success")
