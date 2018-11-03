from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include
from . import views

urlpatterns = [
    url('', views.index, name = 'index')
]
