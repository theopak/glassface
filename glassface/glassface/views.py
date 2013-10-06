from glassface.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.shortcuts import HttpResponseRedirect
from glassface.models import GlassfaceUser
import urllib, urllib2, time, os, json, random, string
from social.apps.django_app.default.models import UserSocialAuth
from glassface import settings

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

def logins(request):
    user = request.user
    context = {
        'twitter_connected': False,
    }
    return TemplateResponse(request, "logins/index.html", context)

def twitteradd(request, uidtofollow):
    usertoadd = User.get(pk=uidtofollow)
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

    twitter.create_friendship(user_id=user_to_follow)

    context = {

    }

    return TemplateResponse(request, "logins/twitter/connect.html", context)
