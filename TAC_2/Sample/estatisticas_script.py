"""
autora: Julia Ferraz
data: 17/02/2021
versão: 1
"""

### importações de bibliotecas internas do Python.
import csv

# Printa o valor máximo encontrado no arquivo "filename" na coluna "coluna"
# (str, int) --> None
def valor_maximo(filename: str, coluna: int):
    maximo = -99999999999999
    with open(filename, "r") as arquivo_csv:
        if filename[-3:].lower() == "csv":
            delimitador = ","
        else:
            delimitador = "\t"
        arquivo = csv.reader(arquivo_csv, delimiter=delimitador)
        arquivo.__next__()  # Pula a primeira linha, que é o cabeçalho
        for row in arquivo:
            try:
                valor = float(row[coluna - 1])
                if valor > maximo:
                    maximo = valor
                else:
                    pass
            except ValueError:
                print("a coluna selecionada não contém dados válidos")
                return None
    print("máximo = {}" .format(maximo))

# Printa a média dos valores encontrados no arquivo "filename" na coluna "coluna"
# (str, int) --> None
def media(filename: str, coluna: int):
    soma = 0
    numeros_lidos = 0
    with open(filename, "r") as arquivo_csv:
        if filename[-3:].lower() == "csv":
            delimitador = ","
        else:
            delimitador = "\t"
        arquivo = csv.reader(arquivo_csv, delimiter=delimitador)
        arquivo.__next__()              # Pula a primeira linha, que é o cabeçalho
        for row in arquivo:
            try:
                valor = float(row[coluna - 1])
                soma += valor
                numeros_lidos += 1
            except ValueError:
                print("a coluna selecionada não contém dados válidos")
                break
    try:
        print("média = {}" .format(soma / numeros_lidos ))
    except ZeroDivisionError:
        print("Não é possível dividir por zero")

# Printa o valor mínimo encontrado no arquivo "filename" na coluna "coluna"
# (str, int) --> None
def valor_minimo(filename: str, coluna: int):
    minimo = 99999999999999
    with open(filename, "r") as arquivo_csv:
        if filename[-3:].lower() == "csv":
            delimitador = ","
        else:
            delimitador = "\t"
        arquivo = csv.reader(arquivo_csv, delimiter=delimitador)
        arquivo.__next__()  # Pula a primeira linha, que é o cabeçalho
        for row in arquivo:
            try:
                valor = float(row[coluna - 1])
                if valor < minimo:
                    minimo = valor
                else:
                    pass
            except ValueError:
                print("a coluna selecionada não contém dados válidos")
                return None
    print("mínimo = {}" .format(minimo))

# Printa a razao entre os valores encontrados nas colunas 1 e 2
# (str, int) --> None
def razao(filename: str, identificador: int, coluna1: int, coluna2: int):
    identificador -= 1
    coluna1 -= 1
    coluna2 -= 1
    with open(filename, "r") as arquivo_csv:
        if filename[-3:].lower() == "csv":
            delimitador = ","
        else:
            delimitador = "\t"
        arquivo = csv.reader(arquivo_csv, delimiter=delimitador)
        arquivo.__next__()                             # Pula a primeira linha, que é o cabeçalho
        for row in arquivo:
            try:
                razao = float(row[coluna1])  /  float(row[coluna2])
                print(row[identificador] + "\t{}".format(razao) )
            except ZeroDivisionError:
                print("Não é possivel dividir por zero, essa razão não é válida")
            except ValueError:
                print("a coluna selecionada não contém dados válidos")
                break
