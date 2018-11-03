# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm
from .forms import RegisterForm


# Create your views here.
def index(request):

	username = "not logged in"


	if request.method == 'POST':
	        login_form = LoginForm(request.POST)
	        register_form = RegisterForm(request.POST)
	        if form.is_valid():
	            pass  # does nothing, just trigger the validation
	else:
		login_form = LoginForm()
		register_form = RegisterForm()
	return render(request, 'mainApp/index.html', {'login_form' : login_form, 'register_form':register_form, 'username':username})


	   
