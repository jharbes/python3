# Retornar qual letra aparece o maior numero de vezes na string utilizando while na solucao.

frase='O Python é uma linguagem de programação multiparadigma. Python foi criado por Guido van Rossum.'

contador=0
numeroMaximoRepeticoes=0
caracatereMaisRepetido=''

while (len(frase)<contador):
    letraTestada=frase[contador]
    if frase.count(frase[contador])>numeroMaximoRepeticoes:
        numeroMaximoRepeticoes=frase.count(frase[contador])
        caracatereMaisRepetido=frase[contador]
    contador+=1

print(f'O caractere que mais apareceu foi o')
print()
