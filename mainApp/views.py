# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import LoginForm
from .forms import RegisterForm
from mainApp.models import User

# Create your views here.
def index(request):
	login_form = LoginForm()
	register_form = RegisterForm()

	if request.method == 'POST':
		if 'login-submit' in request.POST:
			login_form = LoginForm(request.POST)
			email = request.POST.get("email_login", None)
			password = request.POST.get("password_login", None)

			if login_form.is_valid():
				user = authenticate(email = email, password = password)

				if user is not None:
				    login(request, user)
				    if request.user.is_staff:
			       		return redirect('/admin/')
				    else:
				       return redirect("home/")
			else:
				return render(request, 'mainApp/index.html', {'login_form' : login_form, 'register_form':register_form, 'state':1})

		elif 'register-submit' in request.POST:
			register_form = RegisterForm(request.POST)
			email = request.POST.get("email_register", None)
			password = request.POST.get("password_register", None)

			if register_form.is_valid():
				register_form.save()
				user = authenticate(email = email, password = password)
				subject = 'SketchPass'
				message = 'Thank you for signing up to SketchPass '
				from_email = settings.EMAIL_HOST_USER
				to_list = [user.email]
				send_mail (subject,message,from_email,to_list,fail_silently=True)
				send_mail (subject,message,from_email,to_list,fail_silently=True)
				if user is not None: #error checking to make sure inserted correctly
					login(request, user)
					if request.user.is_staff:
						return redirect('/admin/')
					else:
						return redirect("home/")
			else:
				return render(request, 'mainApp/index.html', {'login_form' : login_form, 'register_form':register_form, 'state':2})
	else:
		login_form = LoginForm()
		register_form = RegisterForm()
	return render(request, 'mainApp/index.html', {'login_form' : login_form, 'register_form':register_form, 'state':0})
