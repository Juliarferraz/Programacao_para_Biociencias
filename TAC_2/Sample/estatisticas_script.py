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
            valor = float(row[coluna - 1])
            if valor > maximo:
                maximo = valor
            else:
                pass
    print("máximo Total_recovered = {}" .format(maximo))

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
            valor = float(row[coluna - 1])
            float('16,94'.replace(',', '.'))
            soma += valor
            numeros_lidos += 1
    print("média Total_cases = {}" .format(soma / numeros_lidos ))

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
            valor = float(row[coluna - 1])
            if valor < minimo:
                minimo = valor
            else:
                pass
    print("mínimo Total_deaths = {}" .format(minimo))

# Printa a razao entre os valores encontrados nas colunas 1 e 2
# (str, int) --> None
def razao(filename: str, identificador: int, coluna1: int, coluna2: int):
    identificador -= 1
    coluna1 -= 1
    coluna2 -= 1
    print("Country	 Total_cases/Total_deaths")
    with open(filename, "r") as arquivo_csv:
        if filename[-3:].lower() == "csv":
            delimitador = ","
        else:
            delimitador = "\t"
        arquivo = csv.reader(arquivo_csv, delimiter=delimitador)
        arquivo.__next__()                             # Pula a primeira linha, que é o cabeçalho
        for row in arquivo:
            razao = float(row[coluna1])  /  float(row[coluna2])
            print(row[identificador] + "\t{}".format(razao) )