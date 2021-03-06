from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'glassface.views.splash', name='home'),
    url(r'^twitteradd/([a-zA-Z0-9]+)$', 'glassface.views.twitteradd'),
    #url(r'^process$', 'glassface.views.'),
    # url(r'^glassface/', include('glassface.foo.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': "/"}),
    url(r'^accounts/signup/$', 'glassface.views.create_user'),

    url(r'^test_google/(?P<google_user_id>[^/]+)/(?P<circle_id>[^/]+)/$','glassface.views.add_to_circle'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^facebook/add/(.+)/$', 'glassface.facebookfriender.views.add'),
    url(r'^linkfacebook/$', 'glassface.views.linkfacebook'),    
    url(r'^destroy/(?P<backend>[^/]+)/$','glassface.views.destroy',name='destroy'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social')),

    # inputs from the app
    url(r'^app_login/$', 'glassface.views.app_login'),
    url(r'^app_identify/$', 'glassface.views.app_identify'),
    url(r'^app_confirm/$', 'glassface.views.app_confirm'),
)
