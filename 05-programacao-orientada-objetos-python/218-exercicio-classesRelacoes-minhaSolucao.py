# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self,nome) -> None:
        self._nome=nome
        self._motor=None
        self._fabricante=None

    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self,nome):
        self._nome=nome

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,motor):
        self._motor=motor

    @property
    def fabricante(self):
        return self._fabricante
    
    @fabricante.setter
    def fabricante(self,fabricante):
        self._fabricante=fabricante


class Motor:
    def __init__(self,tipo) -> None:
        self.tipo=tipo


class Fabricante:
    def __init__(self,nome) -> None:
        self.nome=nome


carro=Carro('Golf GTI')
carro.motor='1.5 turbo'
carro.fabricante='Volkswagen'

print(vars(carro))
print(carro.__dict__)