a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

string0 = 'a={} b={} c={}'
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

print(string0.format(a,b,c))
print(string)

formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)