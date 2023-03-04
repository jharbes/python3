# if / elif      / else
# se / se não se / se não
# python importante usar o : (dois pontos) , parenteses sao opcionais nas condicoes e nao se usa else if e sim elif
entrada = input('Você quer "entrar" ou "sair"? ')

if (entrada == 'entrar'):
    print('Você entrou no sistema')

    print(12341234)
elif entrada == 'sair': 
    print('Você saiu do sistema')
else:
    print('Você não digitou nem entrar e nem sair.')

print('FORA DOS BLOCOS')