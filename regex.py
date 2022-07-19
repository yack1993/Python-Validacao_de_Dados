#expressões regulares;
from TelefonesBr import TelefonesBr
import re
#padrao = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"
#texto = "aaabbbcc rodrigo123@gmail.com.br"
#m = re.search(padrao,texto)
#print(m.group())

#padrao_molde = "(xx)aaaa-wwww"
#padrao1 = "[0-9]{2}[0-9]{4,5}[0-9]{4}"
#texto = "eu gosto do numero 2126451234"

#resp = re.search(padrao1,texto)
#print(resp.group())

#----------------------------------

telefone = "552126481234"

telefone_objeto = TelefonesBr(telefone)
print(telefone_objeto)

