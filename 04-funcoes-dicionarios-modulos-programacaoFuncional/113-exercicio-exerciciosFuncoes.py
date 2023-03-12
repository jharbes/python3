# Exercícios com funções

# Crie uma função que multiplica todos os argumentos
# não nomeados recebidos
# Retorne o total para uma variável e mostre o valor
# da variável.

def multiplica(*args):
    totalMultiplicacao=1
    for numero in args:
        totalMultiplicacao*=numero
    return totalMultiplicacao

variavel1=multiplica(2,3,4,5,6)
print(variavel1)




# Crie uma função fala se um número é par ou ímpar.
# Retorne se o número é par ou ímpar.

def parOuImpar(numero):
    return f'{numero} é um número é par' if numero%2==0 else f'{numero} é um número é ímpar'

print(parOuImpar(15))
print(parOuImpar(14))
print(parOuImpar(-4))
