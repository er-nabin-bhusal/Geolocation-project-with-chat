from __future__ import unicode_literals

from django.db import models

# Create your models here.

from django.conf import settings


class ChatClass(models.Model):
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='owner') #this is done to avoid errors with dual foreignkeys
	opponent = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='opponent')
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True,)
	anything = models.CharField(max_length=100,default="Can we be Friends?")
	friends = models.BooleanField(default=False)

	def __unicode__(self):
		return "send from %s to %s" % (self.owner,self.opponent)

	def __str__(self):
		return "send from %s to %s" % (self.owner,self.opponent)



class MessageClass(models.Model):
	sender = models.ForeignKey(settings.AUTH_USER_MODEL,related_name="sender")
	user_set = models.ForeignKey(ChatClass,related_name="didicatedusers")
	message = models.CharField(max_length=200)
	timestamp = models.DateTimeField(auto_now_add=True,null=True)

	def __unicode__(self):
		return "sender is %s in the group %s" %(self.sender,self.user_set)

	def __str__(self):
		return "sender is %s in the group %s" %(self.sender,self.user_set)