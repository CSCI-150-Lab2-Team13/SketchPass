from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add/', views.website_form, name = 'add'),
    url(r'^logout/', views.logout_view, name='logout'),
]
