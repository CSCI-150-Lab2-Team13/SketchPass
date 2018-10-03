from django.conf.urls import url
from sketchtools import views


urlpatterns = [
	path('', views.index, name='index')
]