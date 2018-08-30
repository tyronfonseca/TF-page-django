from django.conf.urls import url
from django.views.generic import TemplateView
from website.views import *

urlpatterns = [
	url(r'^$', AboutView.as_view()),
	url(r'^gender/$',gender),
    url(r'^work/$', WorksView.as_view()),
    url(r'^work/(?P<adv>[\w\-]+)/$', WorkView),
    url(r'^contact/$',ContactoView.as_view())
]
