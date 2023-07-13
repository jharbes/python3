from funcoesAuxiliares import formatacaoMoeda
import Conta

class ContaPoupanca(Conta):

    def sacar(self,valor):
        if self.saldo>=valor:
            self.saldo-=valor
            self.detalhes('SAQUE VALOR {}'.format(formatacaoMoeda(valor)))
        else:
            self.detalhes('SALDO INSUFICIENTE')