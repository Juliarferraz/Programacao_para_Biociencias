"""
autora: Julia Ferraz
data: 24/02/2021
versão: 1
"""
# Programa que recebe uma sequência de DNA e
# imprime a sequência de mRNA e a proteína correspondente

from Bio.Seq import Seq

DNA = Seq(str(input("Digite uma sequencia de DNA: ")))

DNA= DNA.upper()
DNA = DNA.complement()
mRna = DNA.transcribe()
proteina = DNA.translate()

print("A sequencia do mRna é {}".format(mRna))
print("A proteína respectiva é {}".format(proteina))
