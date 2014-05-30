from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'origamio.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),
    url(r'^signin/', 'origamio.views.signin', name='signin'),
    url(r'^signup/', 'origamio.views.signup', name='signup'),
    url(r'^lost/', 'origamio.views.lost', name='lost'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    # Line for python-social-auth
    url('', include('social.apps.django_app.urls', namespace='social')),
)
