from django.urls import path

from .views import GeneroCreate, GeneroLista, GeneroUpdate, HomeView
from .views import IdiomaCreate, IdiomaLista, IdiomaUpdate
from .views import AutorCreate, AutorLista, AutorUpdate
from .views import UsuarioCreate, UsuarioLista, UsuarioUpdate
from .views import LivroCreate, LivroLista, LivroUpdate
from .views import EmprestimoCreate, EmprestimoLista, EmprestimoUpdate, EmprestimoDetailsView
from .views import ReservaCreate, ReservaLista, ReservaUpdate, pie_chart

urlpatterns = [
    path('',HomeView.as_view(),name='index'),
    path('index/',HomeView.as_view(),name='index'),
]    
urlpatterns += [        
    #Gênero
    path('cadastrar/genero',GeneroCreate.as_view(), name='cadastrar-genero'),
    path('editar/genero/<int:pk>/',GeneroUpdate.as_view(), name='editar-genero'),        
    path('listas/formListarGenero/', GeneroLista.as_view(),name="listar-genero"),
]
urlpatterns += [    
    #Idioma
    path('cadastrar/idioma',IdiomaCreate.as_view(), name='cadastrar-idioma'),
    path('editar/idioma/<int:pk>/',IdiomaUpdate.as_view(), name='editar-idioma'),        
    path('listas/formListarIdioma/', IdiomaLista.as_view(),name="listar-idioma"),
]
urlpatterns += [    
    #Autor
    path('cadastrar/autor',AutorCreate.as_view(), name='cadastrar-autor'),
    path('editar/autor/<int:pk>/',AutorUpdate.as_view(), name='editar-autor'),        
    path('listas/formListarAutor/', AutorLista.as_view(),name="listar-autor"),
]
urlpatterns += [    
    #Usuário
    path('cadastrar/usuario',UsuarioCreate.as_view(), name='cadastrar-usuario'),
    path('editar/usuario/<int:pk>/',UsuarioUpdate.as_view(), name='editar-usuario'),        
    path('listas/formListarUsuario/', UsuarioLista.as_view(),name="listar-usuario"),    
]
urlpatterns += [    
    #Livro
    path('cadastrar/livro',LivroCreate.as_view(), name='cadastrar-livro'),
    path('editar/livro/<int:pk>/',LivroUpdate.as_view(), name='editar-livro'),        
    path('listas/formListarLivro/', LivroLista.as_view(),name="listar-livro"),
]    
urlpatterns += [    
    #Emprestimo
    path('cadastrar/emprestimo',EmprestimoCreate.as_view(), name='cadastrar-emprestimo'),
    path('editar/emprestimo/<uuid:pk>/',EmprestimoUpdate.as_view(), name='editar-emprestimo'),        
    path('listas/formListarEmprestimo/', EmprestimoLista.as_view(),name="listar-emprestimo"),
    path('emprestimo/<uuid:pk>/detalhes/',EmprestimoDetailsView.as_view(),name='emprestimo-detalhes'),
]      
urlpatterns += [    
    #Reserva
    path('cadastrar/reserva',ReservaCreate.as_view(), name='cadastrar-reserva'),
    path('editar/reserva/<int:pk>/',ReservaUpdate.as_view(), name='editar-reserva'),        
    path('listas/formListarReserva/', ReservaLista.as_view(),name="listar-reserva"),
]      
urlpatterns+=[
    path('get/ajax/QtdeEstoque', EmprestimoCreate.pegaEstoqueLivro, name = "pegaEstoque")
]
#Grafico
urlpatterns+=[
    path('livro-chart/',pie_chart, name='livro-chart'), 
]   