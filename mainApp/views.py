# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.conf import settings
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import LoginForm
from .forms import RegisterForm
from .tokens import account_activation_token
from mainApp.models import User
from django import forms

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
			form = RegisterForm(request.POST)

			if form.is_valid():
				#create inactive user with no password
				##user = authenticate(email = email, password = password)
				user =register_form.save(commit = False)
				user.is_active = False
				user.save()
				#send email to user with token
				mail_subject = 'Welcome to SketchPass'
				current_site = get_current_site (request)
				message = render_to_string ('activate_email.html',{
				'user':user,
				'domain':current_site.domain,
				'uid': urlsafe_base64_encode(force_bytes(user.pk)),
				'token': account_activation_token.make_token(user),
				})
				to_email = form.cleaned_data.get('email_register')
				email = EmailMessage(mail_subject, message, to=[to_email])
				email.send()
				return HttpResponse('Please confirm your email address to complete the registration')
			else:
				return render(request, 'mainApp/index.html', {'login_form' : login_form, 'register_form':register_form, 'state':2})
	else:
		login_form = LoginForm()
		register_form = RegisterForm()
	return render(request, 'mainApp/index.html', {'login_form' : login_form, 'register_form':register_form, 'state':0})

def activate (request,uidb64,token):
	try:
		uid = force_text(urlsafe_base64_decode(uidb64))
		user = User.objects.get(pk=uid)
	except (TypeError, ValueError, OverflowError, User.DoesNotExist):
		user = None
	if user is not None and account_activation_token.check_token(user, token):
		user.is_active = True
		user.save()
		login(request, user)
		# return redirect('home')
		return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
	else:
		 return HttpResponse('Activation link is invalid!')
