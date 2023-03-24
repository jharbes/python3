# LIST COMPREHENSION

# list comprehension faz as mesmas coisas que funcoes map, filter, flatMap de outras linguagens e até mais do que isso.

# List comprehension será usada para por meio de um iterável gerar um outro iterável com algum processamento de dados (alteração, filtro, etc)

numeros=[1,2,3,4,5]
novosNumeros=numeros # nao gera copia! apenas aponta para o mesmo valor na memoria, mudar uma altera as duas (pois o local na memoria pra onde apontam altera os valores)

numeros[0]=20
print(novosNumeros) # [20, 2, 3, 4, 5]

