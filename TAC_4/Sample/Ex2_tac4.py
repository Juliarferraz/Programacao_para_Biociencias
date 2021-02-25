"""
autora: Julia Ferraz
data: 24/02/2021
versão: 1
"""

# programa Python que pegue o arquivo sequencias.fasta e
# escreva N arquivos FASTA contendo
# em cada arquivo apenas uma sequência de sequencias.fasta,
# chamados de sequência_i.fasta (onde i varia de 1 a N)

# importações de bibliotecas internas do Python.
import sys
# importações de bibliotecas externas do Python.
from Bio import SeqIO

#recebe como entrada na linha de comando:
codigo_desconhecido = sys.argv[1]
#abrir arquivo para ser lido
contador = 0
for i in SeqIO.parse(open(codigo_desconhecido),"fasta"):
    contador += 1
    nomeArquivo = str("Sequencia_{}.fasta").format(contador)
    refArquivoSaida = open(nomeArquivo,"w")
    SeqIO.write(i, refArquivoSaida, "fasta")
    refArquivoSaida.close()
print("Pastas foram criadas com sucesso")