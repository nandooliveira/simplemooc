from django.conf.urls import include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^', include('simplemooc.core.urls', namespace='core')),
    url(r'^admin/', include(admin.site.urls)),
]
