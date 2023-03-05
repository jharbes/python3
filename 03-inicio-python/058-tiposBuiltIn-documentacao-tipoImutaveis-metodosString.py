"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""

string = '1000'
outra_variavel = f'{string[:3]}ABC{string[4:]}'
print(string)
print(outra_variavel)  # 100ABC

print(string.zfill(10))  # 0000001000
print(type(string.zfill(10)))  # string
