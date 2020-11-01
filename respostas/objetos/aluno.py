from enum import Enum
from .pessoa import Pessoa

class NivelAlunos(Enum):
    INDEFINIDO = 0
    FUNDAMENTAL = 1
    MEDIO = 2
    GRADUACAO = 3
    MESTRADO = 4
    DOUTORADO = 5
    
    # ToString de Python (chamado pela função str())
    def __str__(self):
        return self.name
    
class Aluno(Pessoa):
    # Construtor com valores default:
    def __init__(self, nome='Indefinido', sexo='I', idade=0, matricula='Indefinida', 
                 nivel=NivelAlunos.INDEFINIDO):        
        # Pessoa.__init__(self)      # chama construtor da classe pai (nao eh necessario)
        self.set_nome(nome)
        self.set_idade(idade)
        self.set_sexo(sexo)
        self.matricula = matricula # propriedade (ver abaixo)
        self.nivel = nivel         # propriedade (ver abaixo)
        
    def __str__(self):
        string_resultante = "Aluno [Nome: " + self.get_nome() + \
        ", Idade: " + str(self.get_idade()) + \
        ", Gênero: " + self.get_sexo() + \
        ", Matrícula: " + self.matricula + \
        ", Nível: " + str(self.nivel) + "]"
        
        return string_resultante 
                   
    @property                    # permite que o atributo seja visto do lado de fora, como uma propriedade 
    def matricula(self):         # propriedades chamam implicitamente o metodo (como um 'getter')  
        return self.__matricula  # veja no main que a propriedade eh acessada como se fosse um atributo normal! 

    @matricula.setter
    def matricula(self, matricula):   # define um metodo 'getter' para a propriedade 
        self.__matricula = matricula  # poderia ter um codigo de validacao...      
    
    @property
    def nivel(self):
        return self.__nivel
       
    @nivel.setter
    def nivel(self, nivel):
        self.__nivel = nivel