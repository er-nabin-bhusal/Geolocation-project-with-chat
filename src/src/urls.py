"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from accounts.views import (
        register_view,
        login_view,
        logout_view,
        profile_create_view,
        profile_detail_view,
        home_view,
        profile_update_view,
        search_view,
        )

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/', admin.site.urls),
  	url(r'^register/$', register_view, name='register'),
    url(r'^login/$', login_view, name='login'),
    url(r'^(?P<pk>\d+)/logout$', logout_view, name='logout'),
    url(r'^(?P<pk>\d+)/create$', profile_create_view, name='create'),
    url(r'^(?P<pk>\d+)/$', profile_detail_view, name='detail'),

    url(r'^(?P<pk>\d+)/edit$', profile_update_view, name='edit'),
    url(r'^(?P<pk>\d+)/(?P<query>\d+)/(?P<religion>[\w-]+)/(?P<age>[\w-]+)$', search_view, name='search'),
    url(r'^chat/', include('chats.urls', namespace='chats')),
    url(r'^(?P<pk>\d+)/', include('photos.urls', namespace='photos')),
    url(r'^$', home_view, name='home'),
    ]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
