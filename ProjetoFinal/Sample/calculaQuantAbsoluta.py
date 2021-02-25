"""
autora: Julia Ferraz
data: 24/02/2021
versão: 1
"""

# importações de bibliotecas internas do Python.
import sys
# importações de bibliotecas externas do Python.
import pandas as pd
#receber planilha
planilha_Excel = sys.argv[1] #Valores_CT.xlsx
#receber os coeficientes m(slope) e o coeficiente b (intercept-y)
coeficiente_m = sys.arg[2]
coeficient_b = sys.argv[3]
#criar dataframe
df = pd.DataFrame(planilha_Excel)
#- Crie um novo dataframe nomeado como “df_q” que contém as colunas
# “Target_Name”, “Stage” “CT” e “Quantity”,
# onde Quantity é calculado para cada RNA de interesse usando a Equação 2.
novo = { "Target_Name”:
        "Stage":
        "CT":
        "Quantity": }
df_g = DataFrame(novo)

