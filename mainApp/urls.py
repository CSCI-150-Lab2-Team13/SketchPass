"""SketchPassSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
# Use include() to add paths from the catalog application

from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.conf.urls import include
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_complete,password_reset_confirm
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^reset-password/$', password_reset, {'template_name': 'reset_password.html'},name= 'reset_password'),
    url(r'^reset-password/done/$',password_reset_done, {'template_name': 'reset_done.html'},name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete,{'template_name': 'reset_complete.html'},name = 'password_reset_complete'),
    url(r'^resend-confirmation/$', views.resend_account_activation, name='resend_account_activation'), 
    url(r'^verified-email/$', TemplateView.as_view(template_name="verified_email.html"), name='verified_email'),
    url(r'^invalid-link/$', TemplateView.as_view(template_name="invalid_password_link.html"), name='invalid_password_link'),
       
]

