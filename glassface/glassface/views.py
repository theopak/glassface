from glassface.forms import UserCreationForm
from django.contrib.auth.models import User
from django.template.response import TemplateResponse
from django.shortcuts import HttpResponseRedirect
from glassface.models import GlassfaceUser

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