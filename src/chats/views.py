from django.shortcuts import (
					render,
					redirect,
					get_object_or_404,
					)
from chats.models import ChatClass , MessageClass
from django.contrib.auth import get_user_model

# Create your views here.

from .forms import ChatForm,MessageForm
from django.contrib import messages
from accounts.models import Profile 
from django.http import Http404,HttpResponseRedirect

User = get_user_model()


def chat_view(request,pk1=None,*args,**kwargs):

	# chat_group = ChatClass.objects.get(pk=pk1)
	chat_group = get_object_or_404(ChatClass,pk=pk1)
	message_list = MessageClass.objects.filter(user_set=chat_group).order_by("timestamp")

	for msg in message_list:
		if request.user != msg.sender:
			msg.seen_case=True
			msg.save()


	if request.user == chat_group.owner or request.user == chat_group.opponent:
		for msg in message_list:
			if request.user != msg.sender:
				msg.seen_case=True
				msg.save()
			
		user = request.user 
		form = MessageForm(request.POST or None)


		if form.is_valid() and user.is_authenticated():
			message = form.save(commit=False)
			message.sender = user
			qs_ = ChatClass.objects.get(pk=pk1)
			message.user_set = qs_
			message.save()
		context = {
			'form':form,
			'message_list':message_list,
		}
		return render(request,"chat.html",context)
	else:
		raise Http404("There is no such request!")

def request_accept_view(request,pk1,*args,**kwargs):
	request_obj = ChatClass.objects.get(pk=pk1)
	request_owner = request_obj.owner
	request_profile = Profile.objects.get(user=request_owner)
	if request_obj.opponent == request.user:
		request_obj.friends = True
		request_obj.save()
	else:
		messages.error("Request Can't be accepted.")
	return HttpResponseRedirect(request_profile.get_absolute_url())


def request_deny_view(request,pk1,*args,**kwargs):
	request_obj = ChatClass.objects.get(pk=pk1)
	request_owner = request_obj.owner
	request_profile = Profile.objects.get(user=request_owner)
	if request_obj.opponent == request.user:
		request_obj.delete()
	else: 
		messages.error("Request can't be denied due to some errors.")
	return HttpResponseRedirect(request_profile.get_absolute_url())





	













