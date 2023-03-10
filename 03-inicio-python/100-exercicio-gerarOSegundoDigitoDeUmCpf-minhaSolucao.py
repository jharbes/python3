"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

# stringCpf=input('Digite o CPF no formato XXX.XXX.XXX-XX: ')
stringCpf='102.310.867-41'

if len(stringCpf)==14 and stringCpf[3]=='.' and stringCpf[7]=='.' and stringCpf[11]=='-':
    try:
        int(stringCpf[0:3])
        int(stringCpf[4:7])
        int(stringCpf[8:11])
        int(stringCpf[12:14])

        stringLimpa=stringCpf.replace('.','').replace('-','')
        print(stringLimpa)

        multiplicadorCpf=10
        somadorCpf=0

        for indice,numero in enumerate(stringLimpa[0:9]):
            somadorCpf+=multiplicadorCpf*int(numero)
            multiplicadorCpf-=1

        primeiroDigitoCpf=(somadorCpf*10)%11 if (somadorCpf*10)%11 <= 9 else 0

        multiplicadorCpf=11
        somadorCpf=0

        for indice,numero in enumerate(stringLimpa[0:10]):
            somadorCpf+=multiplicadorCpf*int(numero)
            multiplicadorCpf-=1

        segundoDigitoCpf=(somadorCpf*10)%11 if (somadorCpf*10)%11 <= 9 else 0

        print('O primeiro digito do CPF digitado é',primeiroDigitoCpf)

        print('O segundo digito do CPF digitado é',segundoDigitoCpf)
    except:
        print('Número de CPF fora da conformidade, favor tentar novamente!')
else:
    print('Número de CPF fora da conformidade, favor tentar novamente!')