"""
autora: Julia Ferraz
data: 20/02/2021
versão: 1
"""

# importações de bibliotecas internas do Python
import sys
# importações de bibliotecas externas do Python
# importações de seus próprios módulos e pacotes
from estatisticas_pandas_script import *

def main():
    nome_do_arquivo = sys.argv[1]

    coluna_min = input("Digite o nome da coluna que você deseja calcular o valor mínimo: ")
    valor_min(nome_do_arquivo, coluna_min)
    coluna_media = input("Digite o nome da coluna que deseja calcular a média: ")
    media(nome_do_arquivo, coluna_media)
    coluna_max = input("Digite o nome da coluna que deseja calcular o valor máximo: ")
    valor_max(nome_do_arquivo, coluna_max)
    soma_total_coluna = input("Digite o nome da coluna que você deseja calcular a soma: ")
    soma_total(nome_do_arquivo, soma_total_coluna)
    valor_de_x = int(input("Digite a quantidade de países com maior número de casos que você deseja visualizar: "))
    topx(nome_do_arquivo, valor_de_x)
    cria_coluna(nome_do_arquivo)

if __name__ == "__main__":
    main()