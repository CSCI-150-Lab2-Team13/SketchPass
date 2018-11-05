# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    """A typical class defining a model, derived from the Model class."""
    userID = models.CharField(max_length=20)
    email = models.CharField(max_length=20)


    # User DB
    # user_id = #models.
    # email
    # image_password = 
    # website array

    #passwordDB
    # user_id
    # website_id
    # password

    # --->Websites Db
    #	user_id
    #	website_id
    #	url
    #	Website name
    #	desc
    # 	email/username
    #	category
    #	
    #	Website Password
    # 	Array of Categories


class Website(models.Model):

    user_ID = models.ForeignKey(Users, on_delete=models.CASCADE)
    website_ID = models.CharField(max_length=20)
    urlNAME = models.CharField(max_length=20)
    websiteName = models.CharField(max_length=20)
    desc = models.CharField(max_length=20)
    category = models.CharField(max_length=20)


class Passwords(models.Model):
    userID = models.ForeignKey(Users, on_delete=models.CASCADE)
    websiteID = models.ForeignKey(Website, on_delete=models.CASCADE)
    # 	[Email, Finance, School, Work,
    #	 Entertainment, Hobbied, Shopping, Misc.]
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    

    # Metadata
 #  class Meta:
  #      ordering = ['-my_field_name']

    # Methods
   # def get_absolute_url(self):
    #    """Returns the url to access a particular instance of MyModelName."""
     #   return reverse('model-detail-view', args=[str(self.id)])

    #def __str__(self):
     #   """String for representing the MyModelName object (in Admin site etc.)."""
     #   return self.field_name