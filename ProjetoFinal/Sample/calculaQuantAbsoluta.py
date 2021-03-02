"""
autoras: Giovanna Lessa e Julia Ferraz
data: 27/02/2021
versão: 1
"""
# importações de bibliotecas internas do Python.
import sys
# importações de bibliotecas externas do Python.
import pandas as pd
#receber planilha
planilha_Excel = sys.argv[1] #Valores_CT.xlsx
#receber os coeficientes m(slope) e o coeficiente b (intercept-y), dada a função y = -3.397186047x + 58.53223295
coeficiente_m = float(sys.argv[2])
coeficiente_b = float(sys.argv[3])
#criar dataframe e ler planilha
df = pd.read_excel(planilha_Excel)
df = pd.DataFrame(df)
# Crie um novo dataframe nomeado como “df_q” que contém as colunas
# “Target_Name”, “Stage” “CT” e “Quantity”,
# onde Quantity é calculado para cada RNA de interesse usando a Equação 2.
df_q = df[['Target_Name', 'Stage']].drop_duplicates()
# adição de uma nova coluna:
df_q['Quantity'] = 10 ** ((df['CT']-coeficiente_b)/coeficiente_m)
# juntar as tabelas (deleção das colunas iguais):
df_qfinal = df.merge(df_q)
# salvar a nova tabela:
df_qfinal.to_excel(r"C:\Users\julia\PycharmProjects\Programacao_para_Biociencias\ProjetoFinal\Data\NovaTabela.xlsx")
#imprime df_q
print(df_qfinal)
#Imprime o nome da amostra (“Sample_Name”), condição (“Stage”) seu valor de CT (“CT”)
# e sua abundância (“Quantity”) que apresentou maior abundância (“Quantity”).
coluna_maior_Quantity = df_qfinal["Quantity"].idxmax()
print(df_qfinal.iloc[coluna_maior_Quantity])