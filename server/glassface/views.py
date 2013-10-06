from glassface.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import HttpResponseRedirect
from glassface.models import GlassfaceUser
from social.apps.django_app.default.models import UserSocialAuth
import requests
import json
import urllib, urllib2, time, os, json, random, string
from social.apps.django_app.default.models import UserSocialAuth
from glassface import settings
import cStringIO
import base64

def create_user(request, user_creation_form=UserCreationForm):
    if request.method == "POST":
        form = user_creation_form(data=request.POST or None)
        if form.is_valid():
            # Okay, security check complete. Log the user in.
            new_user = user_creation_form.save(form) # creates django User
            gfu = GlassfaceUser(user=new_user)
            gfu.save()

            return HttpResponseRedirect("/")
    else:
        form = user_creation_form()

    context = {
        'form': form,
    }
    return TemplateResponse(request, "registration/signup.html", context)

def destroy(request,backend):
    user_auth_to_destroy = UserSocialAuth.objects.get(user=request.user,provider=backend)
    user_auth_to_destroy.delete()
    return HttpResponseRedirect("/") 

def splash(request):
    if request.user.is_authenticated():
        try:
            twitterreg = UserSocialAuth.objects.get(user=request.user, provider="twitter")
        except:
            twitterreg = False

        try:
            googlereg = UserSocialAuth.objects.get(user=request.user, provider="google-oauth2")
        except:
            googlereg = False
        context = {
            'twitter_registered': twitterreg,
            'google_registered': googlereg,
        }
    else:
        context = {
            'guest': True,
        }
    return TemplateResponse(request, "splash.html", context)

def logins(request):
    user = request.user
    context = {
        'twitter_connected': False,
    }
    return TemplateResponse(request, "logins/index.html", context)

def twitteradd(request, usertoadd):
    #usertoadd = User.get(username=uidtofollow)
    twitterauth = UserSocialAuth.objects.get(user=request.user, provider="twitter")
    oauth_consumer_key = settings.SOCIAL_AUTH_TWITTER_KEY
    oauth_token = twitterauth.extra_data['access_token']['oauth_token']
    #oauth_nonce = "91227c2566963d6ae01eb72f974e964a"
    oauth_nonce = "".join([random.choice(string.letters) for i in xrange(32)])
    oauth_signature = "eGxVJXIYoG%2B9ay0A4E7QxnBHHrI%3D"
    #currenttime = "1381017251"
    currenttime = str(int(time.time()))
    #user_to_follow = "15378324"


    from twython import Twython
    twitter = Twython(settings.SOCIAL_AUTH_TWITTER_KEY,
                      settings.SOCIAL_AUTH_TWITTER_SECRET,
                      twitterauth.extra_data['access_token']['oauth_token'],
                      twitterauth.extra_data['access_token']['oauth_token_secret'])

    try:
        useridtofollow = UserSocialAuth.objects.get(user=usertoadd, provider="twitter").extra_data['id']
    except:
        return False

    try:
        twitter.create_friendship(user_id=useridtofollow)
    except:
        return False

    return True

def add_to_circle(request,google_user_id,circle_id):
    print request
    google_api_key = "AIzaSyA8ey1d6QYkcTSxeD2dAeP4B3NafzzS34Y"
    user = request.user
    user_social_auth = UserSocialAuth.objects.get(provider="google-oauth2",user=user)
    r = requests.put("https://www.googleapis.com/plusDomains/v1/circles/"+circle_id
        +"/people?userId="+google_user_id+"&key="+google_api_key,
        headers={"authorization":user_social_auth.extra_data["token_type"]+" "+user_social_auth.extra_data["access_token"]})
    return HttpResponse(r.text)

def process_photo(request):
#def process_photo(request,image):
    #file_like = cStringIO.StringIO(base64.b64decode(image))
    #user = glassface.recognition.recognize(file_like)
    user = User.objects.get(pk=4)
    output = ({})
    output['twitter'] = twitteradd(request, user)
    print output
    return HttpResponse(output)
