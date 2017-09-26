# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'website/pages/home.html')

def networking(request):
    return render(request,'website/pages/networking.html')

def intel(request):
    return render(request,'website/pages/intel.html')

def about(request):
    return render(request,'website/pages/quienes-somos.html')

def microsoft(request):
    return render(request,'website/pages/microsoft.html')

def enterprise(request):
    return render(request,'website/pages/enterprise.html')

def directo(request):
    return render(request,'website/pages/directo.html')

def contacto(request):
    return render(request,'website/pages/contacto.html')

def almacenamiento(request):
    return render(request,'website/pages/almacenamiento.html')

def servers(request):
    return render(request,'website/pages/servers.html')

def torre(request):
    return render(request,'website/pages/torre.html')

def blade(request):
    return render(request,'website/pages/blade.html')

def rack(request):
    return render(request,'website/pages/rack.html')

def compartida(request):
    return render(request,'website/pages/compartida.html')    