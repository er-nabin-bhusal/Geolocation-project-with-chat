from chats.models import ChatClass,MessageClass
from django import forms

class ChatForm(forms.ModelForm):
	class Meta:
		model = ChatClass
		fields = [
				'anything',
				]


class MessageForm(forms.ModelForm):
	class Meta:
		model = MessageClass
		fields = ['message',]
