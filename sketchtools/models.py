# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class MyModelName(models.Model):
    """A typical class defining a model, derived from the Model class."""

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