"""
   Sistema de verifacação de usuarios em uma corretora de investimentos.Utilizando um banco dados simples, seu nome, id, saldo, quantas vezes comprou ou vendeu ações
"""


compras=0
vendas=0
    




#chamando a funçao

def imprimir_nome():
    print(nome)

def imprimir_id():
    print(id)
def imprimir_saldo():
    print(saldo)



def verificar_compras():
    global compras
    compras=int(input('Digite quantas vezes você comprou ações: '))
    if compras==0:
        print('nao comprou açoes')
    else:
        compras+=0
        return compras
    


def verificar_vendas():
    global vendas
    vendas=int(input('Digite quantas vezes você vendeu ações: '))
    if vendas==0:
        print('nao vendeu açoes')
        return vendas
    else:
        vendas+=0
        return vendas

#verificaçao
try:
   nome=str(input('Digite seu nome: '))
   id=int(input('Digite seu id: '))
   saldo=float(input('Digite seu saldo: '))
   imprimir_nome()
   imprimir_id()
   imprimir_saldo()
   print(verificar_compras())
   print(verificar_vendas())
   

except:
    print('Dados inválidos')
else:
    print('tudo ok')


saldo_compra= saldo
operacao_compra = saldo_compra * compras
operacao_venda= saldo_compra - vendas

def compras_açoes():
    compras=int(input('numero de compras: '))
    if compras==0:
        print('nao comprou açoes')
        return compras
    else:
        print(f'seu saldo atual: {operacao_compra}')
        return operacao_compra


def venda_açoes():
    vendas=int(input('numero de vendas: '))
    if vendas==0:
        print('nao vendeu açoes')
        return vendas
    else:
        print(f'seu saldo atual: {operacao_venda} ')
        return operacao_venda


if operacao_compra<0:
    print('invalid')

if operacao_venda<0:
    print('invalid')

print(compras_açoes())
print(venda_açoes())