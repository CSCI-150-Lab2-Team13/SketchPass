# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm
from .forms import RegisterForm
from django.http import JsonResponse
from mainApp.models import Users

# Create your views here.
def index(request):
	login_form = LoginForm()
	register_form = RegisterForm()

	if request.method == 'POST':       
		if 'login-submit' in request.POST:
			login_form = LoginForm(request.POST)
			if login_form.is_valid():
				pass
		elif 'register-submit' in request.POST:
			register_form = RegisterForm(request.POST)
			if register_form.is_valid():
				pass
	else:
		login_form = LoginForm()
		register_form = RegisterForm()
	return render(request, 'mainApp/index.html', {'login_form' : login_form, 'register_form':register_form})


def validate_email(request):
	email = request.GET.get('email', None)
	data = {
		'is_taken': Users.objects.filter(email__iexact=email).exists()
	}

	if data['is_taken']:
		data['error_message'] = 'A user with this email already exists.'
	else:
		data['error_message'] = 'All good!'
	return JsonResponse(data)