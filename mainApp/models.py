# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractUser):
    """User model."""
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager() ## This is the new line in the User model. ##

    """A typical class defining a model, derived from the Model class."""
    #id autoincremenet primary key built in

    # User DB
    # user_id = #models.
    # email
    # image_password =


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
    PASSWORD_CHOICES = (
        ('BUSINESS', 'Business'),
        ('EDUCATION', 'Education'),
        ('ENTERTAINMENT', 'Entertainment'),
        ('FINANCE', 'Finance'),
        ('SOCIAL','Social'),
        ('SHOPPING', 'Shopping'),
        ('NEWS/REFERENCE', 'News/Reference'),
        ('MISCELLANEOUS','Miscellaneous'),
        ('XXXX' , 'xxxx ayy ;)')

    )
    #id
    user_ID = models.ForeignKey(User, on_delete=models.CASCADE)
    #django automatically creates autoincrementing id website_ID = models.CharField(max_length=20)
    password = models.CharField(help_text='Enter field documentation', max_length = 100)
    urlNAME = models.CharField(max_length=100)
    websiteName = models.CharField(max_length=30)
    desc = models.CharField(max_length=250)
    category = models.CharField(max_length= 30,choices=PASSWORD_CHOICES)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.password + '-' + self.websiteName




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
