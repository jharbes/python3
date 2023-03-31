# nos caminhos de sys.path

import moduloTeste
from moduloTeste import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(moduloTeste.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(moduloTeste.soma(2, 3))


print('Este módulo se chama', __name__)
variavel_modulo = 'Luiz'


def soma(x, y):
    return x + y