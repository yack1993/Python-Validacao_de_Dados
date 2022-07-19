import requests

from acesso_cep import BuscarEndereco

cep = "01001000"
c = BuscarEndereco(cep)
#print(c)

bairro, cidade, uf = c.acessa_via_cep()
print("Bairro:{}, Cidade:{}, UF:{}".format(bairro,cidade,uf))

#r = requests.get("https://viacep.com.br/ws/01001000/json/")
#print(r.text)

a = c.acessa_via_cepTeste()
#print(type(a))
#print(dir(a))
#print(a.text)
print(a.json())
#print(a.json()["cep"])

