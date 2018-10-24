# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Users(models.Model):
    """A typical class defining a model, derived from the Model class."""
    userID = models.CharField(max_length=20)
    emailID = models.CharField(max_length=20)


    # Fields
    # user_id = #models.
    # email
    # image_password = #
    # backup_password #
    # website_id
    # --->Websites Db
    #	Website Name
    #	Website Username
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