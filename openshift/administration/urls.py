from django.conf.urls.defaults import *
from django.conf import settings
import os

urlpatterns = patterns('administration.views',

     (r'^$','dashboard'),
      (r'^login_user/$','login_user'),
       (r'^dashboard/$','dashboard'),
      (r'^logout_user/$','logout_user'),
     (r'^salon/', include('administration.salon_admin.urls')),
     (r'^password/', include('administration.password_url')),
     (r'^users/$','view_users'),
     (r'^users/add/$','add_admin'),
     (r'^users/view/(?P<user_id>\d+)/$', 'view_admin'),
     (r'^users/edit/(?P<user_id>\d+)/$', 'edit_admin'), 
     (r'^users/delete/(?P<user_id>\d+)/$', 'delete_admin'),
      
)