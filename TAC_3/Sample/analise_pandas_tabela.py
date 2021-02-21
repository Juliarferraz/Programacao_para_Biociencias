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
    nome_do_arquivo = sys.argv[0]

    coluna_min = input("Digite o nome da coluna que deseja calcular o valor mínimo: ")
    valor_min(nome_do_arquivo, coluna_min)
    coluna_media = input("Digite o nome da coluna que deseja calcular a média: ")
    media(nome_do_arquivo, coluna_media)
    coluna_max = input("Digite o nome da coluna que deseja calcular o valor máximo: ")
    valor_max(nome_do_arquivo, coluna_max)
    soma_total_coluna = input("Digite o nome da coluna que você deseja calcular a média ")
    soma_total(nome_do_arquivo, soma_total_coluna)
    coluna_e_x = input("Digite o nome da coluna que voce deseja e o valor de x")
    topx(nome_do_arquivo, (coluna_e_x[2]),(coluna_e_x[1]))
    cria_coluna(nome_do_arquivo)

if __name__ == "__main__":
    main()