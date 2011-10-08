from django.conf.urls.defaults import *



urlpatterns = patterns('salon.views',
    #(r'^polls/$', 'index'),
     (r'^edit_photo/(?P<salon_id>\d+)/$', 'edit_salon_photo'),
     (r'^edit/(?P<salon_id>\d+)/$', 'edit_salon'),
     (r'^add/$', 'add_salon'),
     (r'^addservice/(?P<pop_up>\w+)/$', 'add_service'),
     (r'^addjob/(?P<pop_up>\w+)/$', 'add_job'),
     (r'^service/(?P<salon_id>\d+)/$', 'salon_services'),
     (r'^service/edit/(?P<service_id>\d+)/$', 'edit_salon_service'),
     (r'^service/add/(?P<salon_id>\d+)/$', 'add_salon_service'),
     (r'^service/delete/(?P<service_id>\d+)/$', 'delete_salon_service'),   
     (r'^(?P<salon_id>\d+)/$', 'detail'),
     (r'^stylist/edit_photo/(?P<stylist_id>\d+)/$', 'edit_stylist_photo'),     
     (r'^stylist/edit/(?P<stylist_id>\d+)/$', 'edit_salon_stylist'),  
     (r'^stylist/(?P<salon_id>\d+)/$', 'salon_team'),
     (r'^stylist/view/(?P<stylist_id>\d+)/$', 'stylistview'),
     (r'^stylist/add/(?P<salon_id>\d+)/$', 'add_stylist'),        
   # (r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),
)