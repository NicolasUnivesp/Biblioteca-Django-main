
import datetime
from django.db import models
from django.db.models.deletion import CASCADE, RESTRICT
from django.db.models.fields import AutoField
from django.contrib.auth.models import Group, User
from django.urls import reverse
import uuid 
from datetime import date, timedelta

# Create your models here.

def user_path(instance, filename):
    return "Usuário {0}/{1}".format(instance.user.id, filename)

class Usuario(models.Model):
    SEXO_CHOICES = [
        ["F", "Feminino"],
        ["M", "Masculino"],
        ["N", "Nenhuma das opções"]
    ]

    STATE_CHOICES = [
        ['AC', 'Acre'], 
        ['AL', 'Alagoas'], 
        ['AP', 'Amapá'],
        ['AM', 'Amazonas'],
        ['BA', 'Bahia'],
        ['CE', 'Ceará'],
        ['DF', 'Distrito Federal'],
        ['ES', 'Espírito Santo'],
        ['GO', 'Goiás'],
        ['MA', 'Maranhão'],
        ['MT', 'Mato Grosso'],
        ['MS', 'Mato Grosso do Sul'],
        ['MG', 'Minas Gerais'],
        ['PA', 'Pará'],
        ['PB', 'Paraíba'],
        ['PR', 'Paraná'],
        ['PE', 'Pernambuco'],
        ['PI', 'Piauí'],
        ['RJ', 'Rio de Janeiro'],
        ['RN', 'Rio Grande do Norte'],
        ['RS', 'Rio Grande do Sul'],
        ['RO', 'Rondônia'],
        ['RR', 'Roraima'],
        ['SC', 'Santa Catarina'],
        ['SP', 'São Paulo'],
        ['SE', 'Sergipe'],
        ['TO', 'Tocantins']
    ]
    
    usuarioID = models.BigAutoField(primary_key=True)
    rg = models.BigIntegerField(unique=True,verbose_name= 'RG')
    nome = models.CharField(max_length=255,verbose_name= 'Nome')   
    sobrenome = models.CharField(max_length=255,verbose_name= 'Sobrenome')   
    nascimento = models.DateField(blank=True, null=True,verbose_name='Data de Nascimento')
    sexo = models.CharField(null=True,max_length=1,choices=SEXO_CHOICES,verbose_name='Sexo')
    telefone = models.CharField(max_length=15 ,blank=True, null = True, verbose_name= 'Telefone')
    celular = models.CharField(max_length=15, blank=True, null = True, verbose_name= 'Celular')
    email1 = models.EmailField(max_length=255, blank=True, null = True, verbose_name= 'Email Principal')
    email2 = models.EmailField(max_length=255,  blank=True, null = True, verbose_name= 'Email Alternativo')
    cep = models.CharField(max_length=9,verbose_name= 'C.E.P.')
    endereco = models.CharField(max_length=255,verbose_name= 'Endereço')
    numero = models.CharField(max_length=6,verbose_name= 'Número')
    bairro = models.CharField(max_length=100,verbose_name= 'Bairro')
    municipio = models.CharField(max_length=50,verbose_name= 'Município')
    estado = models.CharField(max_length=2,choices=STATE_CHOICES,verbose_name='UF')
    serie = models.CharField(blank=True, max_length=50,null=True,verbose_name= 'Série')    
    is_active = models.BooleanField(default=True,verbose_name= '', help_text='Marque para Ativar/Desmarque para Desativar o usuário')
    createdAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Criação')
    updatedAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Modificação')
    usuario = models.OneToOneField(User,on_delete=models.RESTRICT,verbose_name="Usuário Sistema")
    grupo = models.ForeignKey(Group,on_delete=models.RESTRICT, verbose_name="Grupo")
    
    def __str__(self):
        return "{}".format(self.nome)

    class Meta:
        db_table='Usuario'
        
class Genero(models.Model):
    """Model que representa um gênero de um livro (exemplo. Ficção, Tecnologia)."""
    generoID = models.BigAutoField(primary_key=True)
    nome = models.CharField(unique=True,max_length=200,verbose_name="Nome",help_text="Informe um gênero de livro (exemplo. Ficção, Tecnologia)")
    descricao = models.TextField(verbose_name= 'Descrição',help_text="Digite uma descrição do gênero")
    is_active = models.BooleanField(default=True,verbose_name= '', help_text='Marque para Ativar/Desmarque para Desativar o gênero')
    createdAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Criação')
    updatedAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Modificação')
    def __str__(self):        
        return self.nome
    class Meta:
        db_table='Genero'
    
class Idioma(models.Model):
    """Model que representa a linguagem do livro (exemplo Inglês, Português, etc.)"""
    idiomaID = models.BigAutoField(primary_key=True)
    nome = models.CharField(unique=True,verbose_name="Nome",max_length=100,help_text="Informe o idioma do livro (exemplo. Inglês, Português etc.)")
    is_active = models.BooleanField(default=True,verbose_name= '', help_text="Marque para Ativar/Desmarque para Desativar o idioma")
    createdAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Criação')
    updatedAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Modificação')

    def __str__(self):
        return self.nome
    class Meta:
        db_table='Idioma'

class Autor(models.Model):
    """Model que representa o autor."""
    autorID = models.BigAutoField(primary_key=True)
    nome = models.CharField(max_length=100,verbose_name="Nome",help_text="Informe o nome do autor")
    sobrenome = models.CharField(max_length=100, verbose_name="Sobrenome",help_text="Informe o sobrenome do autor")
    dataNascimento = models.DateField(null=True, blank=True, verbose_name="Data de Nascimento",help_text="Informe a data de nascimento do autor")
    dataFalecimento = models.DateField(null=True, blank=True,verbose_name="Data de Falecimento")
    is_active = models.BooleanField(default=True,verbose_name= '', help_text="Marque para Ativar/Desmarque para Desativar o autor")
    createdAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Criação')
    updatedAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Modificação')

    class Meta:
        ordering = ['sobrenome', 'nome']
        db_table='Autor'
    

    def get_absolute_url(self):
        """Retorna a url para acessar o autor."""
        return reverse('autor-detalhes', args=[str(self.id)])

    def __str__(self):        
        return '{0}, {1}'.format(self.sobrenome, self.nome)


class Livro(models.Model):
    livroID = models.BigAutoField(primary_key=True)
    titulo = models.CharField(unique=True,max_length = 100,help_text="Informe o título do Livro", verbose_name= 'Título')
    autor = models.ForeignKey('Autor', on_delete=models.SET_NULL, null=True, help_text="Selecione um autor para o livro",verbose_name="Autor")
    co_autor = models.CharField(max_length = 50, blank = True,verbose_name= 'COAUTOR',help_text="Informe o coautor do livro")
    sumario = models.TextField(max_length=1000, help_text="Informe uma breve descrição do livro",verbose_name="Sumário")
    isbn = models.CharField('ISBN', max_length=13,
                            unique=True,                            
                            help_text='13 Caracteres no máximo <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN número</a>')
    genero = models.ForeignKey('Genero', on_delete=models.SET_NULL, null=True, verbose_name="Gênero",help_text="Selecione um gênero para o livro")
    idioma = models.ForeignKey('Idioma', on_delete=models.SET_NULL, null=True,verbose_name="Idioma",help_text="Selecione o idioma do livro")
    quantidade = models.IntegerField(verbose_name='Qtde.',help_text="Informe a Quantidade de livros")
    is_active = models.BooleanField(default=True,verbose_name= '', help_text="Marque para Ativar/Desmarque para Desativar o livro")
    createdAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Criação')
    updatedAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Modificação')
   
    class Meta:
        verbose_name = 'Livro'
        db_table='Livro'
        ordering = ['titulo', 'autor']

    def display_genero(self):
        """Cria uma string para o gênero"""
        return ', '.join([genero.nome for genero in self.genero.all()[:3]])

    display_genero.short_description = 'Gênero'

    def get_absolute_url(self):
        """Retorna a url para acessar os detalhes do livro."""
        return reverse('livro-detalhe', args=[str(self.id)])

    def __str__(self):        
        return self.titulo

class Reserva(models.Model):
    reservaID = models.BigAutoField(primary_key=True)
    livro = models.ForeignKey('Livro', on_delete=models.RESTRICT, null=True,help_text="Selecione o livro a reservar")
    nomeSolicitante = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Usuário",help_text="Selecione o nome do usuário")
    is_active = models.BooleanField(default=True,verbose_name= '', help_text="Marque para Ativar/Desmarque para Cancelar a reserva")    
    dataReserva = models.DateField(default = date.today, verbose_name="Data da Reserva",help_text="Informe a data da reserva do livro")
    createdAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Criação')
    updatedAt = models.DateTimeField(auto_now=True, verbose_name= 'Data de Modificação')
    class Meta:
        verbose_name = 'Reserva'
        db_table='Reserva'
        ordering = ['createdAt']


class Emprestimo(models.Model):   
    dataDevolucaotemp =  date.today()    
    dataDevolucaotemp += timedelta(days = 7)

    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('O', 'Ótimo')
    )
    emprestimoID = models.UUIDField(primary_key=True, default=uuid.uuid4,
                          help_text="ID particular para esse livro")
    livro = models.ForeignKey('Livro', on_delete=models.RESTRICT, null=True,help_text="Selecione o livro a emprestar")
    marca = models.CharField(max_length=200)
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Usuário",help_text="Selecione o nome do usuário")
    dataEmprestimo = models.DateField(default = date.today, verbose_name="Data do Empréstimo",help_text="Informe a data de empréstimo do livro")
    dataPrazoDevolucao = models.DateField(default = dataDevolucaotemp, blank = True, null = True, verbose_name="Data Máxima de Devolução",help_text="Informe a data máxima de devolução do livro")
    dataDevolucao = models.DateField(blank = True, null = True, verbose_name="Data de Devolução",help_text="Informe a data de devolução do livro")
    avaliacao = models.CharField(max_length=1, choices=choices, null=True, blank=True,verbose_name="Avaliação",help_text="Selecione uma avaliação")
    is_active = models.BooleanField(default=True,verbose_name= '', help_text="Marque para Ativar/Desmarque para Desativar o empréstimo")
        
    @property
    def esta_atrasado(self):
        if self.dataPrazoDevolucao and date.today() > self.dataPrazoDevolucao:
            return True
        return False

    STATUS = (
        ('m', 'Manutenção'),
        ('e', 'Emprestado'),
        ('d', 'Disponível'),
        ('r', 'Reservado'),
    )

    status = models.CharField(
        max_length=1,
        choices=STATUS,
        blank=True,
        default='d',
        help_text='Livro Disponível')

    class Meta:
        ordering = ['dataDevolucao']
        permissions = (("Pode Marcar como Devolvido", "Marcar como Devolvido"),)
        db_table='Emprestimos'

    def __str__(self):        
        return '{0} ({1})'.format(self.emprestimoID, self.livro.titulo) 


