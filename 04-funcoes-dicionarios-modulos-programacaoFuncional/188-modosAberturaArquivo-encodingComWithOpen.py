# Leia também: https://www.otaviomiranda.com.br/2020/normalizacao-unicode-em-python/

# with open (context manager) e métodos úteis do TextIOWrapper
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)

caminho_arquivo = '.\\04-funcoes-dicionarios-modulos-programacaoFuncional\\188-aula-criandoArquivo.txt'

with open(caminho_arquivo, 'w+') as arquivo:
    print(type(arquivo))
    print()
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )
    arquivo.seek(0, 0)
    print(arquivo.read())
    print('Lendo')
    arquivo.seek(0, 0)
    print(arquivo.readline(), end='')
    print(arquivo.readline().strip())
    print(arquivo.readline().strip())

    print('READLINES')
    arquivo.seek(0, 0)
    for linha in arquivo.readlines():
        print(linha.strip())


print('#' * 10)

with open(caminho_arquivo, 'r') as arquivo:
    print(arquivo.read())

print('\n-------------------------\n')

# sem o utf8 os caracteres especiais ficarao com erro
with open(caminho_arquivo, 'w', encoding='utf8') as arquivo:
    arquivo.write('Atenção\n')
    arquivo.write('Linha 1\n')
    arquivo.write('Linha 2\n')
    arquivo.writelines(
        ('Linha 3\n', 'Linha 4\n')
    )

with open(caminho_arquivo, 'a', encoding='utf8') as arquivo:
    arquivo.write('Continuação\n')
    arquivo.write('Linha5')

# sem o utf8 os caracteres especiais ficarao com erro
with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
    print(arquivo.read())