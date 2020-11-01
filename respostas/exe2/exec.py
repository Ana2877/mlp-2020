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
    prodPPGCByTipoporAno = df.groupby(['Ano','Qualis'])
    print(prodPPGCByTipoporAno.size().unstack())
    prodPPGCByTipoporAno.size().unstack().plot()
    plt.show()

def exercicio_5(df):
    print(df['Aut.Total'].mean())


def menu():
    menu =  "\n\n0 - Sair\n"+\
            "1 - Número de artigos produzidos por ano\n"+\
            "2 - Número de artigos publicados por ano e por tipo e gráfico\n"+\
            "3 - Número de artigos por categorias\n"+\
            "4 - Número de artigos por categoria e por ano e gráfico\n"+\
            "5 - Número médio de autores por artigo\n\n"
    print(menu)


def main():
    arquivo = 'extratoppgc.csv'
    df = pd.read_csv(arquivo, encoding='cp860',sep=";")

    numero = 9

    while(numero != 0):
        menu()
        numero = int(input())
        if numero>0 and numero<6:
            globals()["exercicio_" + str(numero)](df)

if (__name__ == "__main__"):   
      main()                  