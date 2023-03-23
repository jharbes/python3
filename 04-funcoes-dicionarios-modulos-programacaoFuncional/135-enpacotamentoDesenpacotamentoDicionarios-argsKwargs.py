# Empacotamento e desempacotamento de dicionários
a, b = 1, 2
a, b = b, a
print(a, b) # 2 1

print('----------------------------')

# for chave, valor in pessoa.items():
#     print(chave, valor)

pessoa = {
    'nome': 'Aline',
    'sobrenome': 'Souza',
}

# desempacotamento das keys
a,b=pessoa
print(a,b) # nome sobrenome

# desenpacotamento dos values
a,b=pessoa.values()
print(a,b) # Aline Souza

# ambos os valores, keys e values
a,b=pessoa.items()
print(a,b) # ('nome', 'Aline') ('sobrenome', 'Souza')

(a1, a2), (b1, b2) = pessoa.items()
print(a1, a2) # nome Aline
print(b1, b2) # sobrenome Souza

print('----------------------------')

dados_pessoa = {
    'idade': 16,
    'altura': 1.6,
}

pessoas_completa = {**pessoa, **dados_pessoa}
# print(pessoas_completa)

# args e kwargs
# args (já vimos)
# kwargs - keyword arguments (argumentos nomeados)


def mostro_argumentos_nomeados(*args, **kwargs):
    print('NÃO NOMEADOS:', args)

    for chave, valor in kwargs.items():
        print(chave, valor)


# mostro_argumentos_nomeados(nome='Joana', qlq=123)
# mostro_argumentos_nomeados(**pessoas_completa)

configuracoes = {
    'arg1': 1,
    'arg2': 2,
    'arg3': 3,
    'arg4': 4,
}
mostro_argumentos_nomeados(**configuracoes)