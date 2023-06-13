#lista de ventos historicos e suas datas
eventos=[
    [
        'primeira guerra mundial',
        'segunda guerra mundial',
        'indempendencia do Brasil',
        'indempendencia dos estados unidos',
        'revolução russa',
        'revolução franseça',
        'revolução inglesa',
        'guerra fria'
    ],
    #data de inicio
    [
       1914,
       1939,
       1822,
       1774,
       1917,
       1642,
       1947
    ],
    #da de fim
    [
        1918,
        1945,
        2023,
        2023,
        1923,
        1649,
        1991
    ]
]
data_inicio= eventos[1]
data_fim= eventos[2]
nome_evento= eventos[0]
data_primeira_guerra= eventos[1][0]
def acessar_data_inicio():
    return eventos[1]

def acessar_data_fim():
    return eventos[2]

def acessar_nome():
    return eventos[0]

#chamando as funçoes
print(acessar_data_inicio())
print(acessar_data_fim())
print(acessar_nome())
#verificar se eh inicio de primeira guerra
def verificar_data_inicio_primeira_guerra():
    if data_primeira_guerra==1914 and data_primeira_guerra <= 1918:
        msg=print('primeira guerra mundial')
        return True
    else:
      error=print('evento errado!')
      return False

print(verificar_data_inicio_primeira_guerra())