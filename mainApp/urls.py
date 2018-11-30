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
from django.contrib.auth.views import password_reset,password_reset_done,password_reset_confirm , password_reset_complete
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^reset-password/$', password_reset ,{'template_name': 'reset_password.html'}, name ='reset_password' ),
    url(r'^reset-password/done/$',password_reset_done, name='password_reset_done'),
    url(r'^reset-password/confirm/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',password_reset_confirm, name='password_reset_confirm'),
    url(r'^reset-password/complete/$', password_reset_complete, name = 'password_reset_complete')

]
