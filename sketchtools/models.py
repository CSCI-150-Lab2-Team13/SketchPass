# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

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
    # 	[Email, Finance, School, Work,
    #	 Entertainment, Hobbied, Shopping, Misc.]
    my_field_name = models.CharField(max_length=20, help_text='Enter field documentation')
    

    # Metadata
    class Meta: 
        ordering = ['-my_field_name']

    # Methods
    def get_absolute_url(self):
        """Returns the url to access a particular instance of MyModelName."""
        return reverse('model-detail-view', args=[str(self.id)])
    
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.field_name