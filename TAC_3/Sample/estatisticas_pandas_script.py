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
import xlrd
##para delet

def valor_max(filename:str, coluna):
    arquivo_excel = pandas.read_excel(filename,index = False, header= None)
    coluna_max = arquivo_excel[coluna]
    max_value = coluna_max.max()
    print(max_value)
def valor_min(filename:str, coluna):
    arquivo_excel = pandas.read_excel(filename,index = False, header= None)
    coluna_min = arquivo_excel[coluna]
    min_value = coluna_min.max()
    print(min_value)
    
def media(filename:str, coluna):
    arquivo_excel = pandas.read_excel(filename, header= None)
    coluna_media = arquivo_excel[coluna]
    média = coluna_media.mean()
    print("Média:",média)

def soma_total(filename:str,coluna ):
    arquivo_excel = pandas.read_excel(filename,index = False, header= None)
    coluna_soma = arquivo_excel[coluna]
    soma_coluna = coluna_soma.sum()
    print(soma_coluna)

def topx(filename:str, x: int, coluna ):
    arquivo_excel = pandas.read_excel(filename)
    ordem_decrescente_x = arquivo_excel.sort_values(index= [:x],coluna, ascending=False) #para tornar em ordem decrescente ascending= False
    # printar sem o index (primeira coluna que indica os números das linhas).
    # a função .to_string transforma a váriavel tabular em strings e retira a indexação.
    #print(ordem_decrescente_x.to_string(index=False))
    print(ordem_decrescente_x)

def cria_coluna(filename):
    #criar coluna chamada “Total_cases_per_100mil”
    # normalização por 100.000 habitantes.
    arquivo_excel = pandas.read_excel(filename)
    # [Population] . 1000/100.000 = [Population]/100
    pop_normalizada = arquivo_excel['Population'] / 100
    # calculo da taxa de morte por país.
    # geração de uma nova coluna na tabela existente.
    arquivo_excel['Total_cases_per_100mil'] = arquivo_excel['Total deaths'] / pop_normalizada
    # impressão de apenas duas colunas: Países e a taxa de mortes.
    # pode-se usar .to_csv também, e utilizar sep='\t' para separar as colunas por tabulação.
    print(arquivo_excel[['Country', 'Total_cases_per_100mil']].to_string(index=False))

