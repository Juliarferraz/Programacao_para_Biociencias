"""
autora: Julia Ferraz
data: 20/02/2021
versão: 1
"""

### importações de bibliotecas internas do Python.
### importações de bibliotecas externas do Python
import pandas
import xlrd

def valor_max(filename:str, coluna:str):
    arquivo_excel = pandas.read_excel(filename)
    coluna_max = arquivo_excel[coluna]
    max_value = coluna_max.max()
    print(max_value,'\t\t')
def valor_min(filename:str, coluna:str):
    arquivo_excel = pandas.read_excel(filename)
    coluna_min = arquivo_excel[coluna]
    min_value = coluna_min.min()
    print(min_value,'\t\t')
    
def media(filename:str, coluna:str):
    arquivo_excel = pandas.read_excel(filename)
    coluna_media = arquivo_excel[coluna]
    media = coluna_media.mean()
    print("Média:", media,'\t\t')

def soma_total(filename:str, coluna:str):
    arquivo_excel = pandas.read_excel(filename)
    coluna_soma = arquivo_excel[coluna]
    soma_coluna = coluna_soma.sum()
    print(soma_coluna,'\t\t')

def topx(filename:str, x: int):
    arquivo_excel = pandas.read_excel(filename)
    ordem_decrescente_x = arquivo_excel.sort_values(by=['Total_cases'], ascending=False) #para tornar em ordem decrescente ascending= False
    # printar sem o index (primeira coluna que indica os números das linhas).
    # a função .to_string transforma a váriavel tabular em strings e retira a indexação.
    #print(ordem_decrescente_x.to_string(index=False))
    print(ordem_decrescente_x.iloc[:x].to_string(index = False),'\t\t')

def cria_coluna(filename):
    # normalização por 100.000 habitantes.
    arquivo_excel = pandas.read_excel(filename)
    pop_normalizada = arquivo_excel['Population'] / 100
    # criar coluna chamada “Total_cases_per_100mil”
    arquivo_excel['Total_cases_per_100mil'] = arquivo_excel['Total_deaths'] / pop_normalizada
    print('Quantidade de casos por 100.000 habitantes:\t')
    print(arquivo_excel.to_string(index = False))
