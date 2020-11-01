class Pessoa:
    def __init__(self): # Construtor
        # o parametro 'self' eh o nome que Python da ao atributo 'this' de C++ ou Java 
        # (i.e., refere-se `a  propria instancia).
        # Perceba que self eh declarado em todos os metodos, mas nao eh passado 
        # explicitamente na chamada (ver programa principal). Como em C++, Java e outras LPs, 
        # ele eh passado automaticamente como parametro para todos os metodos de classe. 
        # Assim, o metodo sabe qual instancia ele deve manipular... 
        self.set_idade(0)
        self.set_nome('Indefinido')
        self.set_sexo('I')

    def __str__(self):
        string_resultante = "Pessoa [Nome: " + self.get_nome() + \
        ", Idade: " + str(self.get_idade()) + \
        ", Gênero: " + self.get_sexo() + "]"
        
        return string_resultante 

    def set_nome(self, nome):
        self.__nome = nome   # o atributo inicia com '__' para 'esconde-lo' 

    def set_idade(self, idade):
        self.__idade = idade

    def set_sexo(self, sexo):
        if (sexo == 'I' or sexo == 'i'):
            self.__sexo = 'I'
        elif (sexo == 'M' or sexo == 'm'):
            self.__sexo = 'M'
        elif (sexo == 'F' or sexo == 'f'):
            self.__sexo = 'F'

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade

    def get_sexo(self):
        return self.__sexo