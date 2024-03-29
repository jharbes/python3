# Métodos de classe + factories (fábricas)
# São métodos onde "self" será "cls", ou seja,
# ao invés de receber a instância no primeiro
# parâmetro, receberemos a própria classe.

class Pessoa:
    ano = 2023  # atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    # factorie - metodo que cria uma instancia com alguma particularidade, nao possuem self e sim cls que remete à classe
    @classmethod
    def criar_com_50_anos(cls, nome):
        return cls(nome, 50)

    # factorie - metodo que cria uma instancia com alguma particularidade, nao possuem self e sim cls que remete à classe
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anônima', idade)


p1 = Pessoa('João', 34)
p2 = Pessoa.criar_com_50_anos('Helena')
p3 = Pessoa('Anônima', 23)
p4 = Pessoa.criar_sem_nome(25)

p1.metodo_de_classe() # Hey

print(p2.nome, p2.idade) # Helena 50
print(p3.nome, p3.idade) # Anônima 23
print(p4.nome, p4.idade) # Anônima 25

print('-------------------------')

print(Pessoa.ano) # 2023
Pessoa.metodo_de_classe() # Hey