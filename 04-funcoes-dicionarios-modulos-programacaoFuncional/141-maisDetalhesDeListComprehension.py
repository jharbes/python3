# LIST COMPREHENSION

# list comprehension faz as mesmas coisas que funcoes map, filter, flatMap de outras linguagens e até mais do que isso.

# List comprehension será usada para por meio de um iterável gerar um outro iterável com algum processamento de dados (alteração, filtro, etc)

numeros=[1,2,3,4,5]
novosNumeros=numeros # nao gera copia! apenas aponta para o mesmo valor na memoria, mudar uma altera as duas (pois o local na memoria pra onde apontam altera os valores)

numeros[0]=20
print(novosNumeros) # [20, 2, 3, 4, 5]

print('-------------------------------')

# no caso de dados imutaveis internos (como uma lista de numeros) a copia rasa fornece uma copia completa
numeros2=[1,2,3,4,5]
novosNumeros2=numeros2.copy() # shallow copy/copia rasa
numeros2[0]=20
print(novosNumeros2) # [1, 2, 3, 4, 5]


print('-------------------------------')

numeros3=[1,2,3,4,5]
novosNumeros3=[n for n in numeros3] # list comprehension/gera uma deep copy, copias independentes  mesmo que os dados internos sejam mutaveis 
numeros3[0]=20
print(novosNumeros3) # [1, 2, 3, 4, 5]


# o metodo acima é identico ao de baixo, ambos geram uma deep copy:


numeros4=[1,2,3,4,5]
novosNumeros4=[]
for numero in numeros4:
    novosNumeros4.append(numero)
print(novosNumeros4) # [1, 2, 3, 4, 5]