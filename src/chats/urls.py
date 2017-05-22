from django.conf.urls import url
from chats.views import chat_view 

urlpatterns = [
		url(r'^(?P<pk1>\d+)/chat$', chat_view, name="chat"),
]
