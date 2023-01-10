from django.urls import path # importando da lib
from .views import PaginaInicial, SobreView # importando do arquivo views.py

urlpatterns = [
    # padrão é path('endereco/', minhaview.as_view(),name='nome da url')
    #path('',PaginaInicial.as_view(),name='index'),
    #path('index/',PaginaInicial.as_view(),name='index'),
    path('sobre/', SobreView.as_view(),name='sobre'),
]
