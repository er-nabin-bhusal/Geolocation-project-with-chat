# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from accounts.models import Profile 


def upload_location(instance,filename):
	return "%s/%s" %(instance, filename)


class Picture(models.Model):
	user = models.ForeignKey(Profile,on_delete=models.CASCADE)
	caption = models.CharField(max_length=15,null=True,blank=True)
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	photo = models.ImageField(upload_to=upload_location,null=True,blank=True)
	profile_check = models.BooleanField(default=False)

	def __unicode__(self):
		return "%s-%s" % (self.user,self.caption)


	def __str__(self):
		return "%s-%s" % (self.user,self.caption)

	def get_absolute_url(self):
