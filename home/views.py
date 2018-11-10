# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse
from mainApp.models import User

@login_required
def index(request):
    user= User.objects.get_by_natural_key(request.user)
    # passwords = Website.objects.all()
    websitesValues = user.website_set.values()
    return render(request, 'home/index.html', {'user':user,'website':websitesValues})

