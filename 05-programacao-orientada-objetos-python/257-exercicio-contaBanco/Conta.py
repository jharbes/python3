from abc import ABC, abstractmethod

class Conta(ABC):

    def __init__(self,agencia,numero_conta,saldo) -> None:
        self.agencia=agencia
        self.numero_conta=numero_conta
        self.saldo=saldo

    @abstractmethod
    def sacar(self,valor): ...