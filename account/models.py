# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, email,name, student_id, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            student_id=student_id,
            name=name
        )

        user.password=password
        user.save(using=self._db)
        return user

    def create_superuser(self, email, student_id, name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email=email,
            student_id=student_id,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
        
class Profile(AbstractBaseUser, PermissionsMixin):
    #user = models.OneToOneField(User)
    name = models.CharField(max_length=50,default='null')
    student_id = models.CharField(max_length=9,default='null')
    email = models.EmailField(default='null',unique=True,)
    password = models.CharField(max_length=20,default='null')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)    
    
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','student_id']
   

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):              # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
        
        
      
        
    
