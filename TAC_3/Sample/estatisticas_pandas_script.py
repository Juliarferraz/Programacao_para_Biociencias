"""
autora: Julia Ferraz
data: 20/02/2021
versão: 1
"""

###Cinco funções que calculam e retornam o valor máximo, valor mínimo,  a média e soma total dos valores de uma coluna
### qualquer (use recursos da biblioteca pandas para implementar as funções).
###Uma função que mostra os Top X países com maior número de casos em ordem decrescente,
###onde X é um número inteiro.
###Como os países possuem números populacionais variáveis, devemos normalizar
### a quantidade de casos de COVID pelo total de habitantes.
###Portanto, implemente uma função que normalize o número de casos por 100.000 habitantes e
###adicione numa coluna extra do dataframe original chamada “Total_cases_per_100mil”.


### importações de bibliotecas internas do Python.
### importações de bibliotecas externas do Python
import pandas

"""
def valor_max(filename:str,):
    arquivo_excel = pandas.read_excel(filename)

def valor_min():
    arquivo_excel = pandas.read_excel(filename)
def media():
    arquivo_excel = pandas.read_excel(filename)
"""
def soma_total(filename:str,coluna:int ):
    arquivo_excel = pandas.read_excel(filename)
    soma_coluna = arquivo_excel[coluna].sum()
    print(soma_coluna)
"""
def topX():
    arquivo_excel = pandas.read_excel(filename)

"""