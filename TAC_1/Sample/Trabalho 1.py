def buscahomopolimeros(dna):
    try:
        if dna == '':
            raise TypeError
        dna = dna.upper()
        ultimo_nt = 0
        index_inicio = 0
        comprimento = 1
        lista_homopolimero = []
        for indice in range(len(dna)):
            nt = dna[indice]
            if nt in ["A", "T", "C", "G"]:
                if nt == ultimo_nt:
                    comprimento += 1
                else:
                    if comprimento > 2:
                        lista_homopolimero.append((ultimo_nt, comprimento, index_inicio+1))
                    ultimo_nt = nt
                    index_inicio = indice
                    comprimento = 1
            else:
                raise TypeError
        if comprimento > 2:
            lista_homopolimero.append((ultimo_nt, comprimento, index_inicio+1))
        if lista_homopolimero == []:
            print("Não há homopolimeros")
        else:
            print(lista_homopolimero)

    except:
        print("A sequência inserida é inválida")


buscahomopolimeros("ATAGCAGCTTTT")
buscahomopolimeros('')
buscahomopolimeros('aloATTTC')
buscahomopolimeros('ACTTTTGTCTAAACCCCCCGTCCTATATATAACT')
buscahomopolimeros("atcgtga")
