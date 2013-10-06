from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib import admin
import django_filepicker

import os

class GlassfaceUser(models.Model):
    user = models.ForeignKey(User)
    profile_picture1 = django_filepicker.models.FPFileField(upload_to='uploads')
    profile_picture2 = django_filepicker.models.FPFileField(upload_to='uploads')
    profile_picture3 = django_filepicker.models.FPFileField(upload_to='uploads')
    profile_picture4 = django_filepicker.models.FPFileField(upload_to='uploads')
    profile_picture5 = django_filepicker.models.FPFileField(upload_to='uploads')
    facebook_email = models.CharField(max_length=255, blank=True, null=True)
    facebook_pass = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)

admin.site.register(GlassfaceUser)
