from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin

import os

def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)

class GlassfaceUser(models.Model):
    user = models.ForeignKey(User)
    profile_image = models.FileField(upload_to=get_image_path, blank=True, null=True)

    twitter_oauth_token = models.CharField(max_length=255, blank=True, null=True)
    twitter_oauth_token_secret = models.CharField(max_length=255, blank=True, null=True)

admin.site.register(GlassfaceUser)
