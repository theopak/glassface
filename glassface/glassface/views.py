from glassface.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.shortcuts import HttpResponseRedirect
from glassface.models import GlassfaceUser
from social.apps.django_app.default.models import UserSocialAuth
import requests
import json

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

def twitterconnect(request):
    context = {
        'twitter_connected': False,
    }

    return TemplateResponse(request, "logins/twitter/connect.html", context)

def add_to_circle(request,google_user_id,circle_id):
    print request
    google_api_key = "AIzaSyA6YjQwwDPZ52y8ejL9oemcvAc6rnAwwig"
    user = request.user
    user_social_auth = UserSocialAuth.objects.get(provider="google-oauth2",user=user)
    r = requests.get("https://www.googleapis.com/plusDomains/v1/people/"+google_user_id+"/audiences?key="+google_api_key,
        headers={"authorization":user_social_auth.extra_data["token_type"]+" "+user_social_auth.extra_data["access_token"]})
    print user_social_auth.extra_data["token_type"]+" "+user_social_auth.extra_data["access_token"]
    # r = requests.put("https://www.googleapis.com/plusDomains/v1/circles/"+circle_id
    #     +"/people?userId="+google_user_id+"&key="+google_api_key,
    #     headers={"authorization":user_social_auth.extra_data["token_type"]+" "+user_social_auth.extra_data["access_token"]})
    return HttpResponse(r.text)