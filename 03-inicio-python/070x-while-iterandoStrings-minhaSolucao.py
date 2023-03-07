from unidecode import unidecode

# Retornar qual letra aparece o maior numero de vezes na string utilizando while na solucao.

frase='O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.a'

# colocando em minusculas
fraseLowerSemEspacos=frase.lower()

# retirando todos os caracteres alfanumericos da string
fraseLowerSemEspacos=''.join(ch for ch in fraseLowerSemEspacos if ch.isalnum())

# retirando os acentos das letras (para que letra acentuada posso contar apenas como uma letra normal)
fraseLowerSemEspacos=unidecode(fraseLowerSemEspacos)

contador=0
numeroMaximoRepeticoes=0
caractereMaisRepetido=''
caracateresRepetidos=[]


while (len(fraseLowerSemEspacos)>contador):

    if fraseLowerSemEspacos.count(fraseLowerSemEspacos[contador])>numeroMaximoRepeticoes:

        numeroMaximoRepeticoes=fraseLowerSemEspacos.count(fraseLowerSemEspacos[contador])
        caractereMaisRepetido=fraseLowerSemEspacos[contador]
        caracateresRepetidos.append(fraseLowerSemEspacos[contador])

    # esse elif serve no caso de termos mais de uma letra repetindo-se com o maior numero de vezes, logo todas ficarao como maiores repeticoes
    elif fraseLowerSemEspacos.count(fraseLowerSemEspacos[contador])==numeroMaximoRepeticoes and fraseLowerSemEspacos[contador]!=caractereMaisRepetido:

        if fraseLowerSemEspacos[contador] not in caracateresRepetidos:
            caractereMaisRepetido+=', '+fraseLowerSemEspacos[contador]
            caracateresRepetidos.append(fraseLowerSemEspacos[contador])

    contador+=1


print(f'A(s) letra(s) que mais se repetiu(ram) foi a "{caractereMaisRepetido}" que foi(ram) repetida(s) {numeroMaximoRepeticoes} vezes')

