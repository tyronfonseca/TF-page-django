"""
Definition of urls for TF_Page.
"""

from django.conf.urls import url,include, handler404, handler500
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('website.urls')),
    url(r'^siscon/',include('website-siscon.urls',namespace="siscon")),
	url(r'^api/',include('api.urls',namespace="api")),
]

handler404 = 'website.views.handler404'

handler500 = 'website.views.handler500'
