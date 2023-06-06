"""verificar o paciente ou visitante no hospital tem
       coronavirus 37.5
"""


def verificarSaude(temp):
   if temp > 37.5:
    print("Paciente com coronavirus")
    return temp
   elif temp < 37.5:
    print("Paciente com outra doença")
    return temp
   else:
    print("Paciente sem coronavirus e sem outra doença")
    return temp 



temperature=float(input('insira sua temperatura:'))
print(verificarSaude(temperature))