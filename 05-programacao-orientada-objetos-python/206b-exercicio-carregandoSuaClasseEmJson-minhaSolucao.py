import json

caminhoArquivoJson='.\\05-programacao-orientada-objetos-python\\206-json-arquivoAuxiliar.json'

try:
    with open(caminhoArquivoJson, 'r', encoding='utf8') as arquivo:
        cadastroLista = json.load(arquivo)

except:
    print('Arquivo JSON não localizado, lista inicial de tarefas será vazia.\n')
    cadastroLista=[]


class Pessoa:
    def __init__(self,nome,idade,email,profissao) -> None:
        self.nome=nome
        self.idade=idade
        self.email=email
        self.profissao=profissao


print(cadastroLista)
print(type(cadastroLista[0]))

listaPessoas=[]
for pessoa in cadastroLista:
    print(type(pessoa))
    pessoa=pessoa.replace('{','').replace('}','').replace("'",'').strip()
    print(pessoa)

print(listaPessoas)