nome=input('Digite o seu nome: ')
idade=input('Digite sua idade: ')

if nome!='' or idade!='':
    print(f"Seu nome é {nome}")
    print(f"Seu nome invertido é {nome[::-1]}")
    print('Seu nome contém espaços') if ' ' in nome else print ('Seu nome não contem espaços')
    print(f"Seu nome tem {len(nome)} letras")
    print(f"A primeira letra do seu nome é {nome[0]}")
    print(f"A última letra do seu nome é {nome[len(nome)-1]}")
else:
    print("Desculpe, você deixou campos vazios.")