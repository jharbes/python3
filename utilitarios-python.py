# utilitarios python


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