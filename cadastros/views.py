import sys
from django.http import JsonResponse
from django.shortcuts import render

from django.views.generic import TemplateView
from django.http.response import HttpResponse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from .models import Usuario, Genero, Idioma, Autor, Livro, Emprestimo, Reserva
from django.urls import reverse_lazy, reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import get_object_or_404, render
from datetime import datetime
from django.db.models import Count

#view home
class HomeView(LoginRequiredMixin,ListView):        
    model = Emprestimo
    template_name = './index.html'
    
    def get_queryset(self):                  
        usuariologado = self.request.user    
        if(eh_aluno(usuariologado)):                                        
            emprestimos = Emprestimo.objects.all()
            self.object_list = emprestimos.filter(usuario__usuario=usuariologado)           
        else:
            self.object_list = Emprestimo.objects.all()          
        return self.object_list      

#view do Genero
class GeneroCreate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Genero
    fields = ['nome','descricao','is_active']
    template_name = 'cadastros/formCadastroGenero.html'
    success_url = reverse_lazy('listar-genero')
    success_message = "Gênero Cadastrado com Sucesso !!!"
    error_message = "Erro Cadastrando o Gênero!!!"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-genero')
        return context
   
      
class GeneroUpdate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Genero
    fields = ['nome','descricao','is_active']
    template_name = 'cadastros/formCadastroGenero.html'
    success_url = reverse_lazy('listar-genero')
    success_message = "Gênero Atualizado com Sucesso !!!"
    error_message = "Erro Atualizando o Gênero!!!"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-genero')
        return context

class GeneroLista(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Genero
    template_name = 'listas/formListarGenero.html'

#view do idioma
class IdiomaCreate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Idioma
    fields = ['nome','is_active']
    template_name = 'cadastros/formCadastroIdioma.html'
    success_url = reverse_lazy('listar-idioma')
    success_message = "idioma Cadastrado com Sucesso !!!"
    error_message = "Erro Cadastrando o idioma!!!"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-idioma')
        return context
         
class IdiomaUpdate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Idioma
    fields = ['nome','is_active']
    template_name = 'cadastros/formCadastroIdioma.html'
    success_url = reverse_lazy('listar-idioma')
    success_message = "Idioma Atualizado com Sucesso !!!"
    error_message = "Erro Atualizando o Idioma!!!"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-idioma')
        return context

class IdiomaLista(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Idioma
    template_name = 'listas/formListarIdioma.html'

#view do Autor
class AutorCreate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Autor
    fields = ['nome','sobrenome','dataNascimento','dataFalecimento','is_active']
    template_name = 'cadastros/formCadastroAutor.html'
    success_url = reverse_lazy('listar-autor')
    success_message = "Autor Cadastrado com Sucesso !!!"
    error_message = "Erro Cadastrando o Autor!!!"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-autor')
        return context
   
      
class AutorUpdate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Autor
    fields = ['nome','sobrenome','dataNascimento','dataFalecimento','is_active']
    template_name = 'cadastros/formCadastroAutor.html'
    success_url = reverse_lazy('listar-autor')
    success_message = "Autor Atualizado com Sucesso !!!"
    error_message = "Erro Atualizando o Autor!!!"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-autor')
        return context

class AutorLista(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Autor
    template_name = 'listas/formListarAutor.html'

#view do Usuário
class UsuarioCreate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Usuario
    fields = ['nome','sobrenome','rg','nascimento','sexo','telefone','celular','email1','email2','cep','endereco','numero','bairro','municipio','estado','serie','is_active','usuario','grupo']
    template_name = 'cadastros/formCadastroUsuario.html'
    success_url = reverse_lazy('listar-usuario')
    success_message = "Usuário Cadastrado com Sucesso !!!"
    error_message = "Erro Cadastrando o Usuário!!!"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-usuario')
        return context
   
      
class UsuarioUpdate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Usuario
    fields = ['nome','sobrenome','rg','nascimento','sexo','telefone','celular','email1','email2','cep','endereco','numero','bairro','municipio','estado','serie','is_active','usuario','grupo']
    template_name = 'cadastros/formCadastroUsuario.html'
    success_url = reverse_lazy('listar-usuario')
    success_message = "Usuário Atualizado com Sucesso !!!"
    error_message = "Erro Atualizando o Usuário!!!"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-usuario')
        return context

class UsuarioLista(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Usuario
    template_name = 'listas/formListarUsuario.html'

#view do Livro
class LivroCreate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Livro
    fields = ['titulo','autor','co_autor','sumario','isbn','genero','idioma','quantidade','is_active']
    template_name = 'cadastros/formCadastroLivro.html'
    success_url = reverse_lazy('listar-livro')
    success_message = "Livro Cadastrado com Sucesso !!!"
    error_message = "Erro Cadastrando o Livro!!!"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-livro')
        return context
   
      
class LivroUpdate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Livro
    fields = ['titulo','autor','co_autor','sumario','isbn','genero','idioma','quantidade','is_active']
    template_name = 'cadastros/formCadastroLivro.html'
    success_url = reverse_lazy('listar-livro')
    success_message = "Livro Atualizado com Sucesso !!!"
    error_message = "Erro Atualizando o Livro!!!"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-livro')
        return context

class LivroLista(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador"]
    model = Livro
    template_name = 'listas/formListarLivro.html'

#view do Emprestimo
class EmprestimoCreate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,CreateView):       
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Emprestimo
    fields = ['livro','marca','usuario','dataEmprestimo','dataPrazoDevolucao','dataDevolucao','avaliacao','is_active']
    template_name = 'cadastros/formCadastroEmprestimo.html'
    success_url = reverse_lazy('listar-emprestimo')
    success_message = "Empréstimo Cadastrado com Sucesso !!!"
    error_message = "Erro Cadastrando o Empréstimo!!!"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-emprestimo')
        return context
    
    def pegaEstoqueLivro(request):
        if request.is_ajax and request.method == "GET":            
            livro = request.GET.get("livroid",0) 
            Qtde_livros = Livro.objects.filter(livroID = livro).filter(is_active = True)[0].quantidade
            Qtde_Disponivel = Emprestimo.objects.filter(livro__livroID = livro).filter(dataDevolucao__isnull=True).count()            
            estoquelivro = Qtde_livros - Qtde_Disponivel
            return JsonResponse({"qtdeestoque":estoquelivro}, status = 200)
        return JsonResponse({}, status = 400)

    
class EmprestimoUpdate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,UpdateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador"]
    model = Emprestimo
    fields = ['livro','marca','usuario','dataEmprestimo','dataPrazoDevolucao','dataDevolucao','avaliacao','is_active']
    template_name = 'cadastros/formCadastroEmprestimo.html'
    success_url = reverse_lazy('listar-emprestimo')
    success_message = "Empréstimo Atualizado com Sucesso !!!"
    error_message = "Erro Atualizando o Empréstimo!!!"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-emprestimo')
        return context

class EmprestimoLista(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador",u"Alunos"]
    model = Emprestimo
    template_name = 'listas/formListarEmprestimo.html'

    def get_queryset(self):             
        usuariologado = self.request.user    
        if(eh_administrador(usuariologado)):               
            self.object_list = Emprestimo.objects.all()
        else:
            self.object_list = Emprestimo.objects.filter(usuario__usuario=usuariologado.id)            
        return self.object_list    


class EmprestimoDetailsView(DetailView):
    model = Emprestimo
    template_name = 'base/formDetalhesEmprestimo.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] ="javascript:history.back();"
        return context    


#view do Reserva
class ReservaCreate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,CreateView):
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador",u"Alunos"]
    model = Reserva
    fields = ['nomeSolicitante','livro','dataReserva','is_active']
    template_name = 'cadastros/formCadastroReserva.html'
    success_url = reverse_lazy('listar-reserva')
    success_message = "Reserva Cadastrada com Sucesso !!!"
    error_message = "Erro Cadastrando a Reserva!!!"
    
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-reserva')
        return context
         
class ReservaUpdate(GroupRequiredMixin, LoginRequiredMixin,SuccessMessageMixin,UpdateView):    
    login_url = reverse_lazy('login')    
    group_required = [u"Administrador",u"Alunos"]
    model = Reserva
    fields = ['nomeSolicitante','livro','dataReserva','is_active']
    template_name = 'cadastros/formCadastroreserva.html'
    success_url = reverse_lazy('listar-reserva')
    success_message = "Reserva Atualizada com Sucesso !!!"
    error_message = "Erro Atualizando a Reserva!!!"

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['link'] = reverse_lazy('listar-reserva')
        return context

class ReservaLista(GroupRequiredMixin, LoginRequiredMixin ,ListView):
    login_url = reverse_lazy('login')
    group_required = [u"Administrador",u"Alunos"]
    model = Reserva
    template_name = 'listas/formListarReserva.html'
    def get_queryset(self):             
        usuariologado = self.request.user    
        if(eh_administrador(usuariologado)):               
            self.object_list = Reserva.objects.all()
        else:
            self.object_list = Reserva.objects.filter(nomeSolicitante__usuario=usuariologado)            
        return self.object_list    

#retorna true caso o usuario passado esteja no grupo Administrador
def eh_administrador(user):
    return user.groups.filter(name='Administrador').exists()    

#retorna true caso o usuario passado esteja no grupo Cliente
def eh_aluno(user):        
        return user.groups.filter(name='Alunos').exists()    
#grafico
def pie_chart(request):
    labels = []
    data = []
    title = 'Livros Mais Procurados'
    queryset = Emprestimo.objects.all().values('livro').annotate(total=Count('livro')).values('livro__titulo','total').order_by('livro')
    
    for x in queryset.all():        
        for a,b in x.items():
            #return HttpResponse(a.title())                   
            if a.title() == 'Livro__Titulo':
                labels.append(b.title())
            elif a.title() == 'Total':                   
                data.append(b)     
           
    return render(request, 'listas/Grafico.html', {
            'labels': labels,
            'data': data,
            'titulo': title
    })
