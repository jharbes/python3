import json

caminhoArquivoJson='.\\05-programacao-orientada-objetos-python\\206-json-arquivoAuxiliar.json'

try:
    with open(caminhoArquivoJson, 'r', encoding='utf8') as arquivo:
        cadastro = json.load(arquivo)

except:
    print('Arquivo JSON não localizado, lista inicial de tarefas será vazia.\n')
    listas={
        'todoList':[],
        'refazerList':[]
    }

cadastro={}




class Pessoa:
    def __init__(self,nome,idade,email,profissao) -> None:
        self.nome=nome
        self.idade=idade
        self.email=email
        self.profissao=profissao