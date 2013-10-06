import os
import platform
import subprocess

from django.http import HttpResponse
from django.conf import settings

def add(request, friend):
    phantomjs = os.path.join(settings.PROJECT_PATH, 'glassface', 'facebookfriender', platform.system(), 'phantomjs')
    script =  os.path.join(settings.PROJECT_PATH, 'glassface', 'facebookfriender', 'facebookfriender.js')
    subprocess.call([phantomjs, script, friend, request.user.get_profile().facebook_email, request.user.get_profile().facebook_pass])
    return HttpResponse("woooooo")