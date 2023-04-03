# quando a importacao for por meio do comando:
# from moduloTestePackage.moduloTeste157 import *
# poderemos usar o comando abaixo pra dizer o que sera efetivamente importado (__all__ = *), na ausencia dela o mesmo comando importara tudo que estiver no codigo do modulo
__all__ = [
    'variavel',
    'soma_do_modulo',
    'nova_variavel',
]

variavel = 'Alguma coisa'


def soma_do_modulo(x, y):
    return x + y


nova_variavel = 'OK'