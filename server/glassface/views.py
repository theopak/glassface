
from glassface.facebookfriender.views import extract
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
from glassface import recognition
from django.contrib.auth import authenticate

from requests import Session, Request

def create_user(request, user_creation_form=UserCreationForm):
    if request.method == "POST":
        form = user_creation_form(data=request.POST or None)
        #if form.is_valid():
            # Okay, security check complete. Log the user in.
        new_user = user_creation_form.save(form) # creates django User
        gfu = GlassfaceUser(user=new_user,profile_picture1=form.cleaned_data.get('profile_url1'),
            profile_picture2=form.cleaned_data.get('profile_url2'),
            profile_picture3=form.cleaned_data.get('profile_url3'),
            profile_picture4=form.cleaned_data.get('profile_url4'),
            profile_picture5=form.cleaned_data.get('profile_url5'))
        gfu.save()
        recognition.learn(new_user,[urllib.unquote(gfu.profile_picture1.url),urllib.unquote(gfu.profile_picture2.url),
            urllib.unquote(gfu.profile_picture3.url),urllib.unquote(gfu.profile_picture4.url),urllib.unquote(gfu.profile_picture5.url)])
        return HttpResponseRedirect("/")
        print form.is_valid()
    else:
        form = user_creation_form()

    context = {
        'form': form,
    }
    return TemplateResponse(request, "registration/signup.html", context)

def destroy(request,backend):
    if backend == "facebook":
        gfu = GlassfaceUser.objects.get(user=request.user)
        gfu.facebook_email = ""
        gfu.facebook_pass = ""
        gfu.facebook_id = ""
    else:
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
            'profile_url':urllib.unquote((GlassfaceUser.objects.get(user=request.user).profile_picture1.url))
        }
        print context["profile_url"]
    else:
        print request.user
        context = {
            'guest': True,
        }
    return TemplateResponse(request, "splash.html", context)

# def logins(request):
#     user = request.user
#     context = {
#         'twitter_connected': False,
#     }
#     return TemplateResponse(request, "logins/index.html", context)

def linkfacebook(request):
    context = {}
    if request.POST:
        print request.POST
        gfu = GlassfaceUser.objects.get(user=request.user)
        gfu.facebook_email = request.POST['email']
        gfu.facebook_pass = request.POST['password']
        gfu.facebook_id = extract(request)
    return TemplateResponse(request, "linkfacebook.html", context)

def twitteradd(request, usertoadd):
    #usertoadd = User.get(username=uidtofollow)
    twitterauth = UserSocialAuth.objects.get(user=request.user, provider="twitter")
    if twitterauth is None:
        return False
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
    google_api_key = "AIzaSyA8ey1d6QYkcTSxeD2dAeP4B3NafzzS34Y"
    user = request.user
    user_social_auth = UserSocialAuth.objects.get(provider="google-oauth2",user=user)

    r = requests.put("https://www.googleapis.com/plusDomains/v1/circles/"+circle_id
        +"/people",
        params={"userId":google_user_id,"key":google_api_key},
        headers={"authorization":user_social_auth.extra_data["token_type"]+" "+user_social_auth.extra_data["access_token"]})
    return HttpResponse(r.text)

def app_login(request):
    return HttpResponse("FRAK")
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    print username
    print password
    response = {}
    if user is not None:
        response['result'] = 'success'
    else:
        response['result'] = 'fail'
    return HttpResponse(json.dumps(response), content_type="application/json")

def app_identify(request):
    print request.user
    file_like = cStringIO.StringIO(base64.b64decode(request.POST['image']))
    usertoadd = glassface.recognition.recognize(file_like)
    #user = User.objects.get(pk=4)
    response = {}
    response['user'] = usertoadd.get_full_name()
    response['uid'] = usertoadd.pk
    response['match'] = 'True'
    return HttpResponse(json.dumps(response), content_type="application/json")

def app_confirm(request):
    print request.user
    response = {}
    response['connected'] = {}
    usertoadd = User.objects.get(pk=request.POST['uid'])
    response['connected']['twitter'] = twitteradd(request, usertoadd)
    # Facebook add
    # G+ add
    return HttpResponse(json.dumps(response), content_type="application/json")

    # uid
    # username
    # { connected: {'facebook', 'twitter'} }