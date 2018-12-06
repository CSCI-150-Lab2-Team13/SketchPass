# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import resolve_url
from django.contrib.auth.tokens import default_token_generator
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
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.http import JsonResponse,HttpResponseRedirect
from django.template.response import TemplateResponse
from django.views.decorators.debug import sensitive_post_parameters
from .forms import LoginForm
from .forms import RegisterForm
from .forms import ResendActivationLinkForm
from .forms import ResetPasswordForm
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

                if user is not None and user.is_active:
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
                #create inactive user with no password
                ##user = authenticate(email = email, password = password)
                user =register_form.save(commit = False)
                user.is_active = False
                user.save()
                #send email to user with token
                current_site = get_current_site (request)
                mail_subject = 'Welcome to SketchPass'
                message = render_to_string ('mainApp/activate_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk).decode()),
                'token': account_activation_token.make_token(user),
                })
                to_email = register_form.cleaned_data.get('email_register')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return redirect("home/")
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
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request,'activate_complete.html')
    else:
        return render(request,'invalid_link.html')

def resend_account_activation(request):
    if request.method == 'POST':
        form = ResendActivationLinkForm(request.POST)
        if form.is_valid():
            active_user = User._default_manager.filter(**{
                '%s__iexact' % User.get_email_field_name(): form.cleaned_data['email'],
                'is_active': False,
            })
            if active_user:
                print('****************************')
                print(active_user[0])
                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('activate_email.html', {
                    'user': active_user[0],
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(active_user[0].pk)).decode(),
                    'token': account_activation_token.make_token(active_user[0]),
                })
                active_user[0].email_user(subject, message)
                return redirect("/home")
            else:
                return redirect("/home")
    else:
        print("else")
        form = ResendActivationLinkForm()
    print("ending before render")
    return render(request, 'resend_email.html', {'form': form})


@sensitive_post_parameters()
@never_cache
def password_reset_confirm(request, uidb64, token):
    """
        View that checks the hash in a password reset link and presents a
        form for entering a new password.
    """
    uid = force_text(urlsafe_base64_decode(uidb64))
    user = User.objects.get(pk=uid)
    try:
        reset_form = ResetPasswordForm(instance=user)
        # urlsafe_base64_decode() decodes to bytestring on Python 3
    except (TypeError, ValueError, OverflowError, user.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        validlink = True
        title = ('Enter new password')
        if request.method == 'POST':
            if 'password-submit' in (request.POST):
                reset_form = ResetPasswordForm(request.POST,instance=user)
                password = request.POST.get("password_reset", None)
             
                if reset_form.is_valid():
                    user=reset_form.save(commit = False)
                    user.save()
                    return HttpResponseRedirect('/')
        else:
            reset_form = ResetPasswordForm(instance=user)
    else:
        validlink = False
        reset_form = ResetPasswordForm(instance=user)
        title = ('Password reset unsuccessful')
    context = {
        'reset_form': ResetPasswordForm,
        'title': title,
        'validlink': validlink,
    }
    return render(request, 'reset_confirm.html', context, {'reset_form': ResetPasswordForm})


