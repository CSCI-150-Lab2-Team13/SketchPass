# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

@login_required
def index(request):
    return render(request, 'home/index.html', {})