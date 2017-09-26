from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$',views.index, name ='index'),
    url(r'^networking/$',views.networking, name ='networking'),
    url(r'^intel/$',views.intel, name ='intel'),
    url(r'^quienes-somos/$',views.about, name ='about'),
    url(r'^microsoft/$',views.microsoft, name ='microsoft'),
    url(r'^enterprise/$',views.enterprise, name ='enterprise'),
    url(r'^siscon-directo/$',views.directo, name ='siscon_directo'),
    url(r'^contacto/$',views.contacto, name ='contacto'),
    url(r'^servidores/$',views.servers, name ='servers'),
    url(r'^servidores/torre/$',views.torre, name ='torre'),
    url(r'^servidores/blade/$',views.torre, name ='blade'),
    url(r'^servidores/rack/$',views.torre, name ='rack'),
    url(r'^servidores/compartida/$',views.torre, name ='compartida'),
    ]