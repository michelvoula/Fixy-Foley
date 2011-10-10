from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
import os
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
   (r'^$','public.views.index'),
                           (r'^administration/', include('administration.urls')),  
                                                  (r'^salon/', include('salon.urls')),               
                      (r'^login/$', 'auth.views.login_user'),
                      (r'^public/logout/$', 'public.views.logout_user'),
                      (r'^public/login/$', 'public.views.login_user'),
                      (r'^post/display/(?P<post_id>\d+)/$', 'fixy_cms.views.display_post'),
                      (r'^createpost/$', 'fixy_cms.views.createpost'),
                       (r'^insertimage/$', 'fixy_cms.views.createpost'),
                       (r'^display_photo_album/(?P<album_id>\d+)/?$', 'medias.views.display_photo_album'),
                       (r'^display_video_album/(?P<album_id>\d+)/?$', 'medias.views.display_video_album'),
                       (r'^add/(?P<model_name>\w+)/?$', 'tekextensions.views.add_new_model'),
                       (r'^add_album/(?P<model_name>\w+)/?$', 'tekextensions.views.add_new_album'),                       
                       (r'^addVideo/(?P<video_type>\w+)/?$', 'tekextensions.views.add_new_video'),
                      (r'^i18n/', include('django.conf.urls.i18n')),
                       (r'^admin/', include(admin.site.urls)),
                       
(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(settings.PROJECT_DIR, 'media') }),
(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': os.path.join(settings.PROJECT_DIR, 'admin') }),
    url(r'^password_reset$', 'django.contrib.auth.views.password_reset', {'template_name': 'admin/registration/password_reset_form.html', 'email_template_name':'admin/registration/password_reset_email.html'}),
    url(r'^password_reset_done$', 'django.contrib.auth.views.password_reset_done', {'template_name': 'admin/registration/password_reset_done.html'}),
    url(r'^password_reset_confirm/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)$', 'django.contrib.auth.views.password_reset_confirm', {'template_name': 'admin/registration/password_reset_confirm.html'}),
    url(r'^password_reset_complete$', 'django.contrib.auth.views.password_reset_complete', {'template_name': 'admin/registration/password_reset_complete.html'}),
 
)
