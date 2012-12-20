from django.conf.urls.defaults import patterns
from django.conf import settings

urlpatterns = patterns('',
    (r'^list/$', 'files.views.listfiles'),
    (r'^download/(?P<fileid>\d+)/(?P<secret>\w{%i})/$'% settings.FILE_SECRET_LENGTH, 'files.views.download'),
    (r'^append.json/(?P<fileid>\d+)/$', 'files.views.append'),
    (r'^delete/(?P<fileid>\d+)/$', 'files.views.delete'),
    (r'^upload/$', 'files.views.upload'),
    (r'^upload.json/$', 'files.views.upload', {'json': True}),
    #(r'^$', 'files.views.listfiles'),
)
