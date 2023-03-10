"""
Operação ternária (condicional de uma linha)
<valor> if <condicao> else <outro valor>
"""
condicao = 10 == 11 # false
variavel = 'Valor' if condicao else 'Outro valor' # Outro valor
print(variavel) # Outro valor

print('-------------------------------------')

digito = 9  # > 9 = 0
novo_digito = digito if digito <= 9 else 0 # 9
novo_digito = 0 if digito > 9 else digito
print(novo_digito) # 9

print('----------------------------------')


print('Valor' if False else 'Outro valor' if False else 'Fim')

print('----------------------------------')

x=4
print('deu certo') if x == 2 else print('deu errado')