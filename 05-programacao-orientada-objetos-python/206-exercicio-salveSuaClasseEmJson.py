# Exercício - Salve sua classe em JSON

# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

cadastro={}

caminhoArquivoJson='.\\05-programacao-orientada-objetos-python\\206-json-arquivoAuxiliar.json'

class Pessoa:
    def __init__(self,nome,idade,email,profissao) -> None:
        self.nome=nome
        self.idade=idade
        self.email=email
        self.profissao=profissao


p1=Pessoa('Jorge Nami Harbes',39,'jharbes@hotmail.com','Software Developer')
cadastro['p1']=f'{p1.__dict__}'
p2=Pessoa('Carolina Ferreira Alcântara',28,'carolalcantara94@gmail.com','Professora de Educação Física')
cadastro['p2']=f'{p2.__dict__}'
p3=Pessoa('Maria Ferreira Barreto',89,'maria@barreto.com','Aposentada')
cadastro['p3']=f'{p3.__dict__}'




with open(caminhoArquivoJson, 'w', encoding='utf8') as arquivo:
    json.dump(
        cadastro,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )