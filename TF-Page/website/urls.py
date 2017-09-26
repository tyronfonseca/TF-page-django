from django.conf.urls import url
from django.views.generic import TemplateView
from website.views import *

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="index.html")),
	url(r'^quien/$', QuienView.as_view()),
    url(r'^proyectos/$', TrabajosView.as_view()),
    url(r'^proyectos/(?P<pk>\d+)/$', DetailTrabajoView.as_view()),
    url(r'^contacto/$',ContactoView.as_view())
]
