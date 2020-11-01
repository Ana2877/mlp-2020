from enum import Enum
import datetime
from .pessoa import Pessoa

HOJE = datetime.datetime.now()

class CategoriaFuncionario(Enum):
    INDEFINIDO = 0
    PROGRAMADOR = 1
    ANALISTA = 2
    GERENTE = 3

    def __str__(self):
        return self.name
    
class Funcionario(Pessoa):
    def __init__(self, nome='Indefinido', sexo='I', idade=0, ingresso=HOJE, 
                 categoria=CategoriaFuncionario.INDEFINIDO):        
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_sexo(sexo)
        self.ingresso = ingresso
        self.categoria = categoria
        
    def __str__(self):
        string_resultante = "Funcionario [Nome: " + self.get_nome() + \
        ", Idade: " + str(self.get_idade()) + \
        ", Gênero: " + self.get_sexo() + \
        ", Ingresso: " + str(self.ingresso) + \
        ", Nível: " + str(self.categoria) + "]"
        
        return string_resultante 
                   
    @property  
    def ingresso(self):        
        return self.__ingresso 

    @ingresso.setter
    def ingresso(self, ingresso):
        self.__ingresso = ingresso if ingresso < HOJE else HOJE
    
    @property
    def categoria(self):
        return self.__categoria
       
    @categoria.setter
    def categoria(self, categoria):
        self.__categoria = categoria