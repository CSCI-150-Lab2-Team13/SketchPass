# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
## from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, login, update_session_auth_hash
from django.contrib.sites.shortcuts import get_current_site
from django.core.urlresolvers import reverse
from django.contrib.auth.tokens import default_token_generator
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
from django.contrib import messages
from .forms import LoginForm
from .forms import RegisterForm
from .forms import PasswordResetForm
from .forms import ResendActivationLinkForm
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
            form = RegisterForm(request.POST)

            if form.is_valid():
                #create inactive user with no password
                ##user = authenticate(email = email, password = password)
                user =form.save(commit = False)
                user.is_active = False
                user.save()
                #send email to user with token
                current_site = get_current_site (request)
                mail_subject = 'Welcome to SketchPass'
                message = render_to_string ('activate_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk).decode()),
                'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email_register')
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
                return redirect("home/")
                messages.add_message(request, messages.SUCCESS, 'Successfully Verified.')
            else:
                return render(request, 'mainApp/index.html', {'login_form' : login_form, 'register_form':register_form, 'state':2})
    else:
        login_form = LoginForm()
        register_form = RegisterForm()
    return render(request, 'mainApp/index.html', {'login_form' : login_form, 'register_form':register_form, 'state':0})





@never_cache
def password_reset_confirm(request, uidb64=None, token=None,
                           template_name='reset_confirm.html',
                           token_generator=default_token_generator,
                           set_password_form=PasswordResetForm,
                           post_reset_redirect=None,
                           current_app=None, extra_context=None):

    """
    View that checks the hash in a password reset link and presents a
    form for entering a new password.
    """

    assert uidb64 is not None and token is not None  # checked by URLconf
    if post_reset_redirect is None:
        post_reset_redirect = reverse('password_reset_complete')
    else:
        post_reset_redirect = resolve_url(post_reset_redirect)
    try:
        # urlsafe_base64_decode() decodes to bytestring on Python 3
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, UserModel.DoesNotExist):
        user = None

    if user is not None and token_generator.check_token(user, token):
        validlink = True
        title = ('Enter new password')
        if request.method == 'POST':
            if 'password-submit' in request.POST:
                reset_form = set_password_form(user,request.POST)
                if reset_form.is_valid():
                    user = reset_form.save(commit= False)
                    user.save()
                    return HttpResponseRedirect(post_reset_redirect)
        else:
            form = set_password_form(user)
    else:
        validlink = False
        form = None
        title = ('Password reset unsuccessful')
    context = {
        'form': form,
        'title': title,
        'validlink': validlink,
    }
    if extra_context is not None:
        context.update(extra_context)

    if current_app is not None:
        request.current_app = current_app

    return TemplateResponse(request, template_name, context)


def activate (request,uidb64,token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user,backend='django.contrib.auth.backends.ModelBackend')
        return render(request,'activate_complete.html')
    else:
         return render(request,'invalid_link.html')



def resend_account_activation(request,template_name='resend_email'):
    if request.method == 'POST':
        form = ResendActivationLinkForm(request.POST)
        if form.is_valid():
            active_users = User._default_manager.filter(**{
                '%s__iexact' % User.get_email_field_name(): form.cleaned_data['email'],
                'is_active': False,
            })
            if active_users:
                print('****************************')
                print(active_users[0])
                current_site = get_current_site(request)
                subject = 'Activate Your MySite Account'
                message = render_to_string('activate_email.html', {
                    'user': active_users[0],
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(active_users[0].pk)).decode(),
                    'token': account_activation_token.make_token(active_users[0]),
                })
                active_users[0].email_user(subject, message)
                return redirect("/home")
            else:
                return redirect("/home")
    else:
        print("else")
        form = ResendActivationLinkForm()
    print("ending before render")
    return render(request, 'resend_email.html', {'form': form})
