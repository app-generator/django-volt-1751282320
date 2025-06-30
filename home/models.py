# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    surname = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Students(models.Model):

    #__Students_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    surname = models.TextField(max_length=255, null=True, blank=True)

    #__Students_FIELDS__END

    class Meta:
        verbose_name        = _("Students")
        verbose_name_plural = _("Students")


class University(models.Model):

    #__University_FIELDS__
    name = models.TextField(max_length=255, null=True, blank=True)
    contact = models.TextField(max_length=255, null=True, blank=True)

    #__University_FIELDS__END

    class Meta:
        verbose_name        = _("University")
        verbose_name_plural = _("University")



#__MODELS__END
