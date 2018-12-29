import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

class BilibiliUser(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(_('email address'), unique=True)

class BilibiliFile(models.Model):
    def get_video_path(instance, filename):
        filename = instance.uuid
        video_path = os.path.join("bilibili/static/videos",filename)
        return video_path
    def get_cover_path(instance, filename):
        filename = "image{}".format(instance.uuid)
        cover_path = os.path.join("bilibili/static/covers/",filename)
        return cover_path

    userId = models.CharField(max_length=30)
    uuid = models.CharField(max_length=30, default="no uuid")
    title = models.CharField(max_length=30, default="no title")
    description = models.CharField(max_length=30)
    uploadVideoFile = models.FileField(upload_to=get_video_path, blank=False,default="NOT Video")
    uploadVideoCover = models.FileField(upload_to=get_cover_path, blank=False, default="NOT Cover")
