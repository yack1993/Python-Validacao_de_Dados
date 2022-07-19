from datas_br import Datas
from datetime import datetime, timedelta
'''
hoje = datetime.today()
hoje_f = hoje.strftime()
print(hoje_f)
print(type(hoje_f))
'''


cadastro = Datas()
print(cadastro.momento_cadastro)
print(cadastro.mes_cadastro())
print(cadastro)
print("Dias cadastrados: {}".format(cadastro.tempo_cadastro()))


'''
hoje = datetime.today()
amanha = datetime.today() + timedelta(days=1)

print(amanha - hoje)
'''



