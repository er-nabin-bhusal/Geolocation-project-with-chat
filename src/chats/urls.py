from django.conf.urls import url
from chats.views import chat_view,request_accept_view,request_deny_view

urlpatterns = [
		url(r'^(?P<pk1>\d+)/chat$', chat_view, name="chat"),
		url(r'^(?P<pk1>\d+)/accept$', request_accept_view, name="accept"),
		url(r'^(?P<pk1>\d+)/deny$', request_deny_view, name="deny"),
]
