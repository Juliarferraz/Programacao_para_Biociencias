"""
autora: Julia Ferraz
data: 24/02/2021
versão: 1
"""

# importações de bibliotecas internas do Python.
import sys
# importações de bibliotecas externas do Python.
from Bio import SeqIO
from Bio.Blast.Applications import NcbiblastxCommandline

#recebe como entrada na linha de comando:
codigo_desconhecido = sys.argv[1]
#para parte Blast:
dataBase = sys.argv[2]
meuOutput = open(r"C:\Users\julia\PycharmProjects\Programacao_para_Biociencias\TAC_4\Data\meuOutput.txt",'w')
#abrir arquivo para ser lido
for i in SeqIO.parse(open(codigo_desconhecido),"fasta"):
    nomeArquivo = str("{}.fasta").format(i.id)
    refArquivoSaida = open(nomeArquivo,"w")
    SeqIO.write(i, refArquivoSaida, "fasta")
    refArquivoSaida.close()
    sequencia = nomeArquivo
    ##mudar##
    meuOutput = r"C:\Users\julia\PycharmProjects\Programacao_para_Biociencias\TAC_4\Data\meuOutput.txt"
    ##mudar##
    refArquivoSaida.close()
    ##mudar##
    blastx_path = r"C:\Program Files\NCBI\blast-2.11.0+\bin\blastx.exe"
    ##mudar##

    linha_de_comando_blastx = NcbiblastxCommandline(cmd=blastx_path, query=sequencia,subject=dataBase, outfmt=6,out=meuOutput, evalue=0.05)
    stdout, stderr = linha_de_comando_blastx()


    print("Executando busca local:")


    print("Fim da busca local...")
    print("__" * 25)

    # Abrindo resultado
    blast_result = open(meuOutput, "r")

    qseqid = 0 #query sequence id
    sseqid = 1 # subject sequence id
    pident = 2
    length = 3
    mismatch = 4
    gapopen = 5
    qstart = 6
    qend = 7
    sstart = 8
    send = 9
    evalue = 10 # expect value
    bitscore = 11 # bit score

    results = blast_result.read()
    s = results.split('\n')
    melhorscore = '0'
    Evalue = 0
    encontrada = '0'

    for linha in s:
        hit = linha.split('\t')
        if len(hit) != 12:
            break
        if float(melhorscore) < float(hit[bitscore]):
            busca = hit[qseqid]
            melhorscore = hit[bitscore]
            Evalue = hit[evalue]
            encontrada = hit[sseqid]
            print("Sequência de busca: %s" % i.id)
            print("Sequência encontrada: %s" % encontrada)
            print("Score = %s" % melhorscore)
            print("E-value = %s" % Evalue)
            print("__" * 25)