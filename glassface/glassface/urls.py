from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'glassface.views.logins', name='home'),
    url(r'^twitterconnect/$', 'glassface.views.twitterconnect', name='home'),
    # url(r'^glassface/', include('glassface.foo.urls')),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/signup/$', 'glassface.views.create_user'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',{'template_name': 'base.html'}),
    url(r'^facebook/add/(.+)/$', 'glassface.facebookfriender.views.add'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url('', include('social.apps.django_app.urls', namespace='social'))
)
