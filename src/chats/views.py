from django.shortcuts import render,redirect
from chats.models import ChatClass , MessageClass
from django.contrib.auth import get_user_model

# Create your views here.

from .forms import ChatForm,MessageForm

User = get_user_model()


def chat_view(request,pk1=None,*args,**kwargs):
	chat_group = ChatClass.objects.get(pk=pk1)
	message_list = MessageClass.objects.filter(user_set=chat_group).order_by("timestamp")
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















