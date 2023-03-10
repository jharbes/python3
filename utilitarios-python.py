# utilitarios python

# ambos abaixo servem apenas para guardar lugar no codigo de algo a ser digitado/desenvolvido posteriormente
... or pass


# confere se uma string possui APENAS números: 
# (***CUIDADO: ele também retornará false para numeros com casas decimais como por exemplo 2.3

stringQualquer.isdigit() # True ou False


"""
Trocar o cursor entre janelas do editor e terminal no vscode

1 - Ctrl + Shift + ' vai abrir o terminal
2 - Ctrl + Tab vai voltar o cursor para a área do Editor
3 - Ctrl + ' vai sai do Editor e voltar pro Terminar
"""


# casas decimais em string no output

nome='jorge'
altura=1.82000
linha_1 = f'{nome} tem {altura:.2f} # output: jorge tem 1.80
print(linha_1)


# shell interativo em python:
# digitar no terminal python -i nome_do_arquivo.py
# quit() ou exit() sai do modo interativo


"""
Interpolação básica de strings (herança de C)
%s - string
%d e %i - int
%f - float
%x (com letras minusculas no hexadecimal) e %X (com letras maiusculas no hexadecimal) - Hexadecimal (ABCDEF0123456789)
%06X - seis digitos hexadecimal com minusculas
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %08X' % (1500, 1500))
print('O hexadecimal de %d é %x' % (1500, 1500))


# operador ternario em python:

print('deu certo') if x == 2 else print('deu errado')



# Tratamento de exceções:

try:
    ...
except:
    ...
    
# ou também:

try:
    ...
except Exception as error:
    print(error)
    ...
    


# for em python (com indice)

for indice,item in enumerate(vetorOuString):
            print(letra)