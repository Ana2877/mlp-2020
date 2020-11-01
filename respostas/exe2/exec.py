import pandas as pd
import matplotlib.pyplot as plt

def exercicio_1(df):
    print(df.groupby('Ano').count()[['Tipo']])


def exercicio_2(df):
    prodPPGCByTipoporAno = df.groupby(['Ano','Tipo'])
    print(prodPPGCByTipoporAno.size().unstack())
    prodPPGCByTipoporAno.size().unstack().plot.bar()
    plt.show()

def exercicio_3(df):
    print(df.groupby('Qualis').count()[['Tipo']])

def exercicio_4(df):
    print(df.groupby(['Ano', 'Qualis']).count()[['Tipo']])


def menu():
    menu =  "\n\n0 - Sair\n"+\
            "1 - Número de artigos produzidos por ano\n"+\
            "2 - Número de artigos publicados por ano por tipo e gráfico\n"+\
            "3 - Número de artigos por categorias\n"+\
            "4 - Número de artigos por categoria e ano"
    print(menu)


def main():
    arquivo = 'extratoppgc.csv'
    df = pd.read_csv(arquivo, encoding='cp860',sep=";")

    numero = 9

    while(numero != 0):
        menu()
        numero = int(input())
        if numero == 1:
            exercicio_1(df)
        if numero == 2:
            exercicio_2(df)
        if numero == 3:
            exercicio_3(df)
        if numero == 4:
            exercicio_4(df)

if (__name__ == "__main__"):   
      main()                  