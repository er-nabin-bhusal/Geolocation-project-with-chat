# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

from accounts.models import Profile

class NotifyUser(models.Model):
	text = models.CharField(max_length=50)
	seen_or_not = models.BooleanField(default=False)
	sender = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='sender')
	receiver = models.ForeignKey(Profile,on_delete=models.CASCADE,related_name='receiver')
	timestamp = models.DateTimeField(auto_now_add=True,null=True)

	def __unicode__(self):
		return "%s %s %s." %(self.sender,self.text,self.receiver)

	def __str__(self):
		return "%s %s %s." %(self.sender,self.text,self.receiver)