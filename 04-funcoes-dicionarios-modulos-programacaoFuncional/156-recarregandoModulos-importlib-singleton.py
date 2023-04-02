import importlib

import moduloTeste156

print(moduloTeste156.variavel)

for i in range(10):
    importlib.reload(moduloTeste156)
    print(i)

print('Fim')
