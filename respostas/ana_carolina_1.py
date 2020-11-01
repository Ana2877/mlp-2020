from objetos import Aluno, Pessoa, Funcionario
import random

NUMERO_DE_PESSOAS = 5
CRIAR_PESSOA = 0
CRIAR_ALUNO = 1
CRIAR_FUNCIONARIO = 2

def dados_ficticios():
    Nomes = ['Ana', 'João', 'Mateus', 'Clara', 'Livia']
    Idades = [23, 21, 24, 35, 17]
    Sexos = ['F', 'M', 'M', 'F', 'F']

    if len(Nomes) < NUMERO_DE_PESSOAS or len(Idades) < NUMERO_DE_PESSOAS or len(Sexos) < NUMERO_DE_PESSOAS:
        raise ValueError('Dados ficticios com tamanho inferior ao número de pessoas.')

    return Nomes, Idades, Sexos


def cria_pessoa(nome, idade, sexo):
    criação_aleatoria = random.randint(0, 2)
    if criação_aleatoria == CRIAR_PESSOA:
        nova_pessoa = Pessoa()
    elif criação_aleatoria == CRIAR_ALUNO:
        nova_pessoa = Aluno()
    elif criação_aleatoria == CRIAR_FUNCIONARIO:
        nova_pessoa = Funcionario()
    
    nova_pessoa.set_nome(nome)
    nova_pessoa.set_idade(idade)
    nova_pessoa.set_sexo(sexo)

    return nova_pessoa


def imprime_pessoas(pessoas):
    for i in range(NUMERO_DE_PESSOAS):
        print(pessoas[i])


def main():
    Nomes, Idades, Sexos = dados_ficticios()

    pessoas = []

    for i in range(NUMERO_DE_PESSOAS):
        nova_pessoa = cria_pessoa(Nomes[i], Idades[i], Sexos[i])
        pessoas.append(nova_pessoa)

    imprime_pessoas(pessoas)
    

if (__name__ == "__main__"):   
      main()                  