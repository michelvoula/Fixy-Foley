from django.conf.urls.defaults import *
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns




urlpatterns = patterns('',
    (r'^login/$', 'auth.views.login_user'),
)