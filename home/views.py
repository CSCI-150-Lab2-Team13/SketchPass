# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#from django.db.models.functions import Lower
from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect
# Create your views here.
from django.http import HttpResponse
from mainApp.models import User, Website
from mainApp import views
from .forms import WebsiteForm, EmailChangeForm
from django.core import serializers
from StringIO import StringIO
import csv
from django.utils.encoding import smart_str


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
        #   state = 3
        if 'copy-password' in request.POST:
            messages.add_message(request, messages.SUCCESS, request.POST.get("copy-password"))

        elif 'copy-username'in request.POST:
            #request.POST.get("copy-username")
            messages.add_message(request, messages.SUCCESS, request.POST.get("copy-username"))
    if request.method == 'GET':
        if "search" in request.GET:
            query = request.GET.get("query", "")
            websitesValues = websitesValues.filter(websiteName__icontains=query).values()

    return render(request, 'home/index.html', {'user':user,'websites':websitesValues, 'state':state})

@login_required
def website_form(request):
    if request.method == "POST":
        form = WebsiteForm(request.POST)
        if form.is_valid():
            site = form.save(False)
            site.user_ID = request.user
            site.save()
            messages.add_message(request, messages.SUCCESS, 'Successfully added website.')
            return redirect("/home")

    else:
        form = WebsiteForm()

    return render(request, 'home/website_form.html', {'website_form': form})

@login_required
def edit_website(request):
    if request.method == 'POST':
        if 'edit-form' in request.POST:
            website_id = request.POST.get("edit-form")
            item = Website.objects.get(pk=website_id)
            edit_form = WebsiteForm(instance=item)
            return render(request, 'home/edit.html', {"website_id": website_id, 'edit_form' : edit_form})
        elif 'edit-submit' in request.POST:
            website_id = request.POST.get("edit-submit")
            item = Website.objects.get(pk=website_id)
            edit_form = WebsiteForm(request.POST, instance=item)
            if edit_form.is_valid():
                edit_form.save()
                messages.add_message(request, messages.SUCCESS, 'Successfully edited website.')
            else:
                edit_form = WebsiteForm(instance=item)
                return render(request, 'home/edit.html', {"website_id": website_id, 'edit_form' : edit_form})
        elif 'edit-delete' in request.POST:
            website_id = request.POST.get("edit-delete")
            item = Website.objects.get(pk=website_id)
            edit_form = WebsiteForm(request.POST, instance=item)
            if edit_form.is_valid():
                item.delete()
                messages.add_message(request, messages.INFO, 'Successfully deleted website.')
    return redirect("/home")

@login_required
def options_view(request):
    if request.method == 'POST':
        if 'delete-all' in request.POST:
                user = User.objects.get(id=request.user.id)
                user.website_set.all().delete()
                messages.add_message(request, messages.INFO, 'Successfully deleted all websites.')
                return redirect("/home")

        elif 'update-email' in request.POST:
            user = User.objects.get(id=request.user.id)
            form = EmailChangeForm(request.POST)
            if form.is_valid():
                new_email = form.cleaned_data['new_email']
                user.email = new_email
                user.save()
                messages.add_message(request, messages.SUCCESS, 'New email: %s' % new_email )
                return redirect("/home")
            else:
                messages.add_message(request, messages.ERROR, 'Email address already used!')
                return redirect('home/options.html')

    user = User.objects.get(id=request.user.id)
    websites = user.website_set.all()
    context = {
        "user": user,
        "websites": websites
    }
    return render(request, "home/options.html", context=context)

# @login_required
# def download_websites(request):

@login_required
def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully logged out.')
    return redirect(views.index)
