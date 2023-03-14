O PyCEP Correios pode ser facilmente instalado com o comando a seguir (apenas para python3):

import pycep_correios

endereco = pycep_correios.consultar_cep('37503130')

print(endereco['end'])
print(endereco['bairro'])
print(endereco['cidade'])
print(endereco['complemento'])
print(endereco['complemento2'])
print(endereco['uf'])
print(endereco['cep'])

from pycep_correios
from pycep_correios.excecao import CEPInvalido

try:
    endereco = pycep_correios.consultar_cep('00000000')
except CEPInvalido as exc:
    print(exc)

    busca por Cep.

    import requests

cep = "20.090-002"

cep = cep.replace("-", "").replace(".", "").replace(" ", "")

if len(cep) == 8:
    link = f'https://viacep.com.br/ws/{cep}/json/'

    requisicao = requests.get(link)

    print(requisicao)

    dic_requisicao = requisicao.json()

    uf = dic_requisicao['uf']
    cidade = dic_requisicao['localidade']
    bairro = dic_requisicao['bairro']
    print(dic_requisicao)
else:
    print("CEP Inválido")
    uf = "SP"
cidade = "SP"
endereco = "Sorocaba

link = f'https://viacep.com.br/ws/{uf}/{cidade}/{endereco}/json/'

requisicao = requests.get(link)
print(requisicao)

dic_requisicao = requisicao.json()
print(dic_requisicao)
