#from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class PaginaInicial(TemplateView):
    template_name = "/base/index.html"

class SobreView(TemplateView):
    template_name = "sobre.html"    
