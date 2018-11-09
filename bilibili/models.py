from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class BilibiliUser(AbstractUser):

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    email = models.EmailField(_('email address'), unique=True)


class BilibiliFile(models.Model):
    userId = models.CharField(max_length=30)
    uuid = models.CharField(max_length=30, default="no uuid")
    title = models.CharField(max_length=30, default="no title")
    description = models.CharField(max_length=30)
    upload = models.FileField(upload_to='../videos', blank=False)
