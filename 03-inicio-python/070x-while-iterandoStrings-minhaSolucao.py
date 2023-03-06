# Retornar qual letra aparece o maior numero de vezes na string utilizando while na solucao.

frase='O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

fraseLowerSemEspacos=frase.lower().replace(' ','').replace('.','')

contador=0
numeroMaximoRepeticoes=0
caractereMaisRepetido=''


while (len(fraseLowerSemEspacos)>contador):

    if fraseLowerSemEspacos.count(fraseLowerSemEspacos[contador])>numeroMaximoRepeticoes:
        numeroMaximoRepeticoes=fraseLowerSemEspacos.count(fraseLowerSemEspacos[contador])
        caractereMaisRepetido=fraseLowerSemEspacos[contador]
    contador+=1


print(f'A letra que mais se repetiu foi a "{caractereMaisRepetido}" que foi repetido {numeroMaximoRepeticoes} vezes')

