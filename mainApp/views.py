# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm
from .forms import RegisterForm


# Create your views here.
def index(request):
	
	login_form = LoginForm()
	register_form = RegisterForm()

	return render(request, 'mainApp/index.html')