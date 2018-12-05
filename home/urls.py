from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import include

from . import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^add/', views.website_form, name = 'add'),
    url(r'^edit/', views.edit_website, name='edit_website'),
    url(r'^logout/', views.logout_view, name='logout_view'),
    url(r'^options/', views.options_view, name='options_view'),
    url(r'^download/', views.download_websites, name='download_websites')
]
