from django.conf.urls import url
from django.views.generic import TemplateView
from website.views import *

urlpatterns = [
    #url(r'^$', TemplateView.as_view(template_name="index.html")),
	url(r'^$', QuienView.as_view()),
	url(r'^gender/$',gender),
    url(r'^work/$', TrabajosView.as_view()),
    url(r'^work/(?P<adv>[\w\-]+)/$', WorkView),
    url(r'^contact/$',ContactoView.as_view())
]
