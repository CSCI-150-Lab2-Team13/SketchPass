# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse
from mainApp.models import User, Website
from .forms import WebsiteForm

@login_required
def index(request):
    user= User.objects.get_by_natural_key(request.user)
    websitesValues = user.website_set.values()
    state = 3
    if request.method == 'POST':
    	if 'a-z' in request.POST:
    		state = 1
    	elif 'category' in request.POST:
    		state = 2
    	#elif 'created' in request.POST:
    	#	state = 3


    return render(request, 'home/index.html', {'user':user,'websites':websitesValues, 'state':state})

@login_required
def website_form(request):
    if request.method == "POST":
        form = WebsiteForm(request.POST)
        if form.is_valid():
            site = form.save(False)
            site.user_ID = request.user
            site.save()
            return redirect("/home")

    else:
        form = WebsiteForm()

    args = {}
    args['website_form'] = form

    return render(request, 'home/website_form.html', args)