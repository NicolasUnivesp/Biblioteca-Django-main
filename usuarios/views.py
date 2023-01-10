from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User,Group
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

# Create your views here.

class UsuarioCreateView(CreateView):
    template_name = "cadastros/formpadrao.html"
    form_class = UsuarioForm
    success_url  = reverse_lazy("login")
    group_required = [u"Administrador"]
    
    def form_valid(self, form):
        grupo = get_object_or_404(Group, name = 'Alunos')
        url = super().form_valid(form)
        self.object.groups.add(grupo)
        self.object.save()
        return url
    
    def get_context_data(self, *args,**kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo']="Cadastro de Novo Aluno"
        context['botao'] = "Cadastrar"
        context['link'] = 'login'        
        return context
    
    
        