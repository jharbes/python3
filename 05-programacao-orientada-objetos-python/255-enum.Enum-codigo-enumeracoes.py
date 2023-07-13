import enum

# Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])


class Direcoes(enum.Enum):
    ESQUERDA = enum.auto()
    DIREITA = enum.auto()
    ACIMA = enum.auto()
    ABAIXO = enum.auto()



print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA) # Direcoes.ESQUERDA Direcoes.ESQUERDA Direcoes.ESQUERDA

print(Direcoes(1).name, Direcoes.ESQUERDA.value) # ESQUERDA 1



def mover(direcao: Direcoes):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao.name} ({direcao.value})')


mover(Direcoes.ESQUERDA) # Movendo para ESQUERDA (1)
mover(Direcoes.DIREITA) # Movendo para DIREITA (2)
mover(Direcoes.ACIMA) # Movendo para ACIMA (3)
mover(Direcoes.ABAIXO) # Movendo para ABAIXO (4)