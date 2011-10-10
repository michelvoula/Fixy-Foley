from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
urlpatterns = patterns('',url(r'^password_reset$', 'django.contrib.auth.views.password_reset', {'template_name': 'registration/password_reset_form.html', 'email_template_name':'registration/password_reset_email.html','post_reset_redirect':'/administration/password/password_reset_done'}),
    url(r'^password_reset_done$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'registration/password_reset_done.html'}),
    url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'registration/password_reset_confirm.html','post_reset_redirect':'/administration/password/password_reset_complete'}),
    url(r'^password_reset_complete$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'registration/password_reset_complete.html'}),)