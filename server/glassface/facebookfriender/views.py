import os
import platform
import subprocess

from django.http import HttpResponse
from django.conf import settings

def add(request, friend):
    phantomjs = os.path.join(settings.PROJECT_PATH, 'glassface', 'facebookfriender', platform.system(), 'phantomjs')
    script =  os.path.join(settings.PROJECT_PATH, 'glassface', 'facebookfriender', 'facebookfriender.js')
    try:
        subprocess.call([phantomjs, script, friend, request.user.get_profile().facebook_email, request.user.get_profile().facebook_pass])
    except:
        return False

    return True

def extract(request):
    phantomjs = os.path.join(settings.PROJECT_PATH, 'glassface', 'facebookfriender', platform.system(), 'phantomjs')
    script =  os.path.join(settings.PROJECT_PATH, 'glassface', 'facebookfriender', 'useridextractor.js')
    print "sexy"
    out = subprocess.check_output([phantomjs, script, request.POST['email'], request.POST['password']])
    print out
    print out
    print out
    return "user id goes here"
