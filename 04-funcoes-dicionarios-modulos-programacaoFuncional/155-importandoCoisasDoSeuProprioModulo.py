# nos caminhos de sys.path

import aula97_m
from aula97_m import soma, variavel_modulo

print('Este módulo se chama', __name__)
# print('Este módulo se chama', __name__)
print(aula97_m.variavel_modulo)
print(variavel_modulo)
print(soma(2, 3))
print(aula97_m.soma(2, 3))
 6  
aula97_m.py
Comment on this file
@@ -1 +1,5 @@
print('Este módulo se chama', __name__)
variavel_modulo = 'Luiz'


def soma(x, y):
    return x + y