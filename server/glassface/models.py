from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.contrib import admin
import django_filepicker

import os

class GlassfaceUser(models.Model):
    user = models.ForeignKey(User)
    profile_picture = django_filepicker.models.FPFileField(upload_to='uploads')
    facebook_email = models.CharField(max_length=255)
    facebook_pass = models.CharField(max_length=255)

admin.site.register(GlassfaceUser)