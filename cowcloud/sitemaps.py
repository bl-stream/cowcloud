# encoding: utf-8
from django.contrib.sitemaps import Sitemap

class StaticSitemap(Sitemap):
    priority = 0.5
    lastmod = None
 
    def items(self):
        return [
                "/",
                "/upload",
                "/contact",
            ]
 
    def location(self, obj):
        return obj[0] if isinstance(obj, tuple) else obj
 
    def changefreq(self, obj):
        return obj[1] if isinstance(obj, tuple) else "monthly"
