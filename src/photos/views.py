# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect

# Create your views here.
from photos.models import Picture
from accounts.models import Profile
from django.contrib import messages 


def individual_picture_view(request,pk,pk1):

	owner = Profile.objects.get(pk=pk)
	photo = Picture.objects.get(pk=pk1)
	template = "individual_photo.html"
	context = {
	'owner':owner,
	'photo':photo,
	}
	return render(request,template,context)

def create_profile_picture_view(request,pk,pk1):
	photo = Picture.objects.get(pk=pk1)
	owner = Profile.objects.get(pk=pk)
	if not request.user == owner.user:
		messages.error(request,"You dont have authority")
		return redirect("/")
	qs_ = Picture.objects.filter(user=owner)
	qs1 = qs_.filter(profile_check=True)
	if qs1.exists():
		existing_pro_image = qs1.first()
		existing_pro_image.profile_check = False
		existing_pro_image.save()
	photo.profile_check = True
	photo.save()
	messages.success(request,"Profile Picture changed successfully")

	return redirect("/")

