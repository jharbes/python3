"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-te de desempacotamento
x, y, *resto = 1, 2, 3, 4
print(x, y, resto)

print('------------------------------')


# def soma(x, y):
#     return x + y

# observe que args é recebido como uma tupla, embora os valores recebidos originalmente nao sejam uma, caso seja necessario alterar os valores dentro da funcao podemos converter a tupla em uma lista com o comando args=list(args) 
def soma(*args):
    total = 0
    print(args, type(args)) 
    for numero in args:
        total += numero
    return total


soma_1_2_3 = soma(1, 2, 3)
print(soma_1_2_3)

soma_4_5_6 = soma(4, 5, 6)
print(soma_4_5_6)

print('------------------------------')

numeros = 1, 2, 3, 4, 5, 6, 7, 78, 10
outra_soma = soma(*numeros)
print(outra_soma)

print(sum(numeros))
print(*numeros)

print('------------------------------')

tupla1=(1,2,3,4)
lista1=[5,6,7,8]

print(sum(tupla1))
print(sum(lista1))