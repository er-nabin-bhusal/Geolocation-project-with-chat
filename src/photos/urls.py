from django.conf.urls import url,include
from photos.views import individual_picture_view,create_profile_picture_view



urlpatterns=[

url(r'^photo/(?P<pk1>\d+)$', individual_picture_view, name='photo'),
url(r'^profile/pic/(?P<pk1>\d+)$', create_profile_picture_view, name='propic'),

]