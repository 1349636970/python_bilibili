import logging
import os
import re
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
        username_length = len(username)
        password_length = len(password)
        if username_length < 8 or password_length < 8 or re.match("^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",
                                                                  email) is None:
            return render(request, "bilibili/register.html",
                          {"title": "Welcome to register", "path": "/register", "type_page": "register"})
        else:
            BilibiliUser.objects.create_user(username, email, password)
            return redirect('backstage/')
    else:
        return render(request, "bilibili/register.html",
                      {"title": "Welcome to register", "path": "/register", "type_page": "register"})


def backstage(request):
    allData = models.BilibiliFile.objects.all()
    myVideoTitle = allData.filter(userId=request.user.id).values_list('title')
    myVideoCover = allData.filter(userId=request.user.id).values_list('uuid')
    myVideo = zip(myVideoTitle, myVideoCover)
    return render(request, "bilibili/backstage.html", {
        "type_page": "backstage_main",
        "myvideo": myVideo
    })


def logout_view(request):
    logout(request)
    websiteurl = request.GET.get('website')
    return redirect(websiteurl)


def uploadvideos(request):
    return render(request, 'bilibili/uploadVideo.html',
                  {"title": "Welcome to Upload Video", "path": "/transfer/",
                   "type_page": "uploadvideos"})


def transfer_station(request):
    video_files = request.FILES.get('videoFile')
    video_title = request.POST.get('VideoTitle')
    video_description = request.POST.get("VideoDescription")
    video_userid = request.POST.get("userID")
    video_cover = request.FILES.get("videoCover")
    video_uuid = str(uuid.uuid4())
    dir_bilibili_file = {'title': video_title, 'description': video_description, 'userId': video_userid,
                         'uuid': video_uuid, 'uploadVideoFile': video_files, 'uploadVideoCover': video_cover}
    models.BilibiliFile.objects.create(**dir_bilibili_file)

    return redirect("/backstage")


def backstage_favorite(request):
    return render(request, "bilibili/backstage.html", {
        "type_page": "backstage_favorite"
    })

def backstage_myvideo(request):
#     code
    pass

def backstage_mychannel(request):
#     code
    pass

def video_handle(request):
    # code
    pass