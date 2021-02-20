"""
autora: Julia Ferraz
data: 20/02/2021
versão: 1
"""

# importações de bibliotecas internas do Python
import sys
# importações de bibliotecas externas do Python
#from pandas import *
# importações de seus próprios módulos e pacotes
from estatisticas_pandas_script import *

def main():
    nome_do_arquivo = sys.argv[1]

    #coluna_minimo = int(input("Digite o número da coluna que deseja calcular o valor mínimo: "))
    #valor_minimo(nome_do_arquivo, coluna_minimo)
    #coluna_media = int(input("Digite o número da coluna que deseja calcular a média: "))
    #media(nome_do_arquivo, coluna_media)
    #coluna_maximo = int(input("Digite o número da coluna que deseja calcular o valor máximo: "))
    #valor_maximo(nome_do_arquivo, coluna_maximo)
    soma_total_coluna = int(input("Digite o número da coluna com o identificador das linhas e os números das duas colunas que você deseja calcular a razão separados por um espaço: "))
    soma_total(nome_do_arquivo, soma_total_coluna)

if __name__ == "__main__":
    main()