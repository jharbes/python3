# Exercício - Salve sua classe em JSON

# Salve os dados da sua classe em JSON
# e depois crie novamente as instâncias
# da classe com os dados salvos
# Faça em arquivos separados.

import json

cadastroLista=[]

caminhoArquivoJson='.\\05-programacao-orientada-objetos-python\\206-json-arquivoAuxiliar.json'

class Pessoa:
    def __init__(self,nome,idade,email,profissao) -> None:
        self.nome=nome
        self.idade=idade
        self.email=email
        self.profissao=profissao


p1=Pessoa('Jorge Nami Harbes',39,'jharbes@hotmail.com','Software Developer')
cadastroLista.append(f'{p1.__dict__}')
p2=Pessoa('Carolina Ferreira Alcântara',28,'carolalcantara94@gmail.com','Professora de Educação Física')
cadastroLista.append(f'{p2.__dict__}')
p3=Pessoa('Maria Ferreira Barreto',89,'maria@barreto.com','Aposentada')
cadastroLista.append(f'{p3.__dict__}')




with open(caminhoArquivoJson, 'w', encoding='utf8') as arquivo:
    json.dump(
        cadastroLista,
        arquivo,
        ensure_ascii=False,
        indent=2,
    )