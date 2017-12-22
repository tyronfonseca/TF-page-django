from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.views.generic import TemplateView, DetailView
from website.models import Info_pagina, Trabajos, Habilidades
from api.models import Gender

class QuienView(TemplateView):
    template_name = "quien.html"

    def get_context_data(self, **kwargs):
       context = super(QuienView, self).get_context_data(**kwargs)

       context['habilidad_web'] = Habilidades.objects.all().filter(tipo = 'web')
       context['habilidad_lan'] = Habilidades.objects.all().filter(tipo = 'lan')
       context['habilidad_app'] = Habilidades.objects.all().filter(tipo = 'app')

       context['page_data'] = Info_pagina.objects.first()

       return context



class TrabajosView(TemplateView):
    template_name = "trabajos.html"

    def get_context_data(self, **kwargs):
        context = super(TrabajosView,self).get_context_data(**kwargs)

        context['page_data'] = Info_pagina.objects.first()
        context['trabajos'] = Trabajos.objects.all()

        return context

class DetailTrabajoView(DetailView):
    template_name = "detail_trabajo.html"
    model = Trabajos

    def get_context_data(self,**kwargs):
        context = super(DetailTrabajoView, self).get_context_data(**kwargs)

        return context

class ContactoView(TemplateView):
    template_name = "contacto.html"

    def get_context_data(self, **kwargs):
        context = super(ContactoView, self).get_context_data(**kwargs)

        context['page_data'] = Info_pagina.objects.first()

        return context

def gender(request):
	data = 'empty'
	if request.method == 'POST':
		name_param = request.POST.get('name_param')
		data = Gender.objects.filter(name=name_param.upper())
	return render(request,'gender.html',{'data':data})

def handler404(request):
        response = render_to_response('errorHandlers/404.html', {},
                                      context_instance=RequestContext(request))
        response.status_code = 404
        return response
def handler500(request):
        response = render_to_response('errorHandlers/500.html', {},
                                      context_instance=RequestContext(request))
        response.status_code = 500
        return response
