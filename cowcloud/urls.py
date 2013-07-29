from django.conf.urls.defaults import *
from django.conf import settings
from django.conf.urls import patterns, include, url

from sitemap import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cowcloud.views.home', name='home'),
    # url(r'^cowcloud/', include('cowcloud.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    (r'^forum/', include('pybb.urls', namespace='pybb')),
    (r'^files/', include('files.urls')),
    (r'^$', include('files.urls')),
    (r'^accounts/', include('registration.backends.default.urls')),
    (r'^accounts/$', 'django.views.generic.simple.direct_to_template', {'template': 'accounts.html'}, 'accounts'),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    #url('imprint', 'cowcloud.views.imprint', name='homepage_imprint'),
	#url('archive', 'cowcloud.views.archive', name='homepage_archive'),
	
    (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/media/img/favicon.ico'}),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}, 'index'),
    (r'^plans/$', 'django.views.generic.simple.direct_to_template', {'template': 'plans.html'}, 'plans'),
    (r'^terms/$', 'django.views.generic.simple.direct_to_template', {'template': 'terms.html'}, 'terms'),
    (r'^faq/$', 'django.views.generic.simple.direct_to_template', {'template': 'faq.html'}, 'faq'),
    #(r'^contact/$', 'django.views.generic.simple.direct_to_template', {'template':'contact.html'}, 'contact' ),
    #url(r'^$', TemplateView.as_view(template_name='home.html')),

    #(r'^moneybookers/status_url/', include('moneybookers.urls')),
    #(r'^moneybookers/cancel/', 'MoneybookersCancel'),
    #(r'^moneybookers/ok/', 'MoneybookersOk'),
    #(r'^order/$', 'View_With_Order'),

    url(r"^r/", include("anafero.urls")),
    (r'^contact/', include('contact_form.urls')),
    url(r'', include('webmaster_verification.urls')),
)

urlpatterns += patterns('django.views.generic.simple', 
	#(r'^robots.txt$', 'direct_to_template', {'template':'robots.txt', 'mimetype':'text/plain'}),
	(r'^google722faf1b2e594e5e.html$', 'direct_to_template', {'template':'google722faf1b2e594e5e.html', 'mimetype':'text/plain'}),
)

urlpatterns += patterns('',
	#(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
    url(r'^sitemap.xml', include('static_sitemaps.urls')),
)

if settings.USE_SAML2:
    urlpatterns += patterns('',
        (r'^saml2/', include('djangosaml2.urls')),
        (r'^idp/', include('saml2idp.urls')),
        (r'^sp/', include('saml2sp.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^storage/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STORAGE_ROOT}),
)

#sitemaps = {
#	'pages':Sitemap(['homepage_imprint', 'homepage_archive']),
#	'blog':FileSitemap, 'site':Sitemap(['cowcloud.org', 'cowcloud.org']),
#}
