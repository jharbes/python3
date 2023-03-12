"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

x = 1


def escopo():
    global x
    x = 10

    def outra_funcao():
        global x
        x = 11
        y = 2
        print(x, y)

    outra_funcao()
    print(x)


print(x)
escopo()
print(x)

# aparentemente nao existe escopo de lacos de repeticao como pode se ver nos exemplos abaixo em python:
if True:
    z=10

vetor=[1,2,3]

for i,item in enumerate(vetor):
    w=item

print(z) # 10
print(i) # 2
print(w) # 3g