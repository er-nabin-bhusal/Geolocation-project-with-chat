from django.contrib import admin
from chats.models import ChatClass,MessageClass

# Register your models here.

admin.site.register(ChatClass)
admin.site.register(MessageClass)
