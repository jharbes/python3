# nos caminhos de sys.path

import moduloTeste
from moduloTeste import soma, variavelModulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)

print(moduloTeste.variavelModulo) # funciona dessa maneira com a importacao implicita de todo o moduloTeste

print(variavelModulo) # funciona com apenas esse nome porque foi feita a importacao explicita dessa variavel acima
print(soma(2, 3))
print(moduloTeste.soma(2, 3))


print('Este módulo se chama', __name__)
variavel_modulo = 'Luiz'

