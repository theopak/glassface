from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib import admin
import django_filepicker

import os

class GlassfaceUser(models.Model):
    user = models.ForeignKey(User)
<<<<<<< HEAD
    profile_image = models.FileField(upload_to=get_image_path, blank=True, null=True)
    facebook_email = models.CharField(max_length=255, blank=True, null=True)
    facebook_pass = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)
=======
    profile_picture = django_filepicker.models.FPFileField(upload_to='uploads')
    facebook_email = models.CharField(max_length=255)
    facebook_pass = models.CharField(max_length=255)
>>>>>>> 13844e18863a69fbf5820afd73209b6ce69817f8

admin.site.register(GlassfaceUser)
