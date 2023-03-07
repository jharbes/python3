# Retornar qual letra aparece o maior numero de vezes na string utilizando while na solucao.

frase='O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.a'

fraseLowerSemEspacos=frase.lower().replace(' ','').replace('.','')

contador=0
numeroMaximoRepeticoes=0
caractereMaisRepetido=''
caracateresRepetidos=[]


while (len(fraseLowerSemEspacos)>contador):

    if fraseLowerSemEspacos.count(fraseLowerSemEspacos[contador])>numeroMaximoRepeticoes:

        numeroMaximoRepeticoes=fraseLowerSemEspacos.count(fraseLowerSemEspacos[contador])
        caractereMaisRepetido=fraseLowerSemEspacos[contador]
        caracateresRepetidos.append(fraseLowerSemEspacos[contador])

    elif fraseLowerSemEspacos.count(fraseLowerSemEspacos[contador])==numeroMaximoRepeticoes and fraseLowerSemEspacos[contador]!=caractereMaisRepetido:

        if fraseLowerSemEspacos[contador] not in caracateresRepetidos:
            caractereMaisRepetido+=', '+fraseLowerSemEspacos[contador]
            caracateresRepetidos.append(fraseLowerSemEspacos[contador])

    contador+=1


print(f'A(s) letra(s) que mais se repetiu(ram) foi a "{caractereMaisRepetido}" que foi(ram) repetida(s) {numeroMaximoRepeticoes} vezes')

