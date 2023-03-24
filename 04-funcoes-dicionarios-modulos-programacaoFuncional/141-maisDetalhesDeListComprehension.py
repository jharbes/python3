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

print('-------------------------------')


# Agora usaremos a list comprehension para fazer uma copia da lista com alteracoes dos valores (semelhante a map)

numeros5=[1,2,3,4,5]
novosNumeros5=[n/2 for n in numeros5] 
multiplicacao=[n*2 for n in numeros5]
quadrado=[n**2 for n in numeros5]
squareRt=[n ** (1/2) for n in numeros5]

print(novosNumeros5) # [0.5, 1.0, 1.5, 2.0, 2.5]
print(multiplicacao) # [2, 4, 6, 8, 10]
print(quadrado) # [1, 4, 9, 16, 25]
print(squareRt) # [1.0, 1.4142135623730951, 1.7320508075688772, 2.0, 2.23606797749979]


print('-------------------------------')


## LIST COMPREHENSION COMO FILTER, para filtragem o IF vem depois do for.

numbers=[1,2,3,4,5,6,7,8,9,10]
newNumbers=[n for n in numbers if n>5]
print(newNumbers) # [6, 7, 8, 9, 10]