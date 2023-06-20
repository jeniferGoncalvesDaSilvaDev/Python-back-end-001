#prevents errors em python-impede que um ero aconteça
#metodo try except
#no try, verifica se ha erro, se nao houver erro, o programa roda. Se houver passa para o except
#no except, mostra o erro, o atributo ValueError, verifica se inseriu um dado incorreto
def somar(x,y):
    return x +y
try:
    numero1=int(input('insira um numero: '))
    numero2=int(input('insira outro numero: '))
    #chamando a funçao
    soma = somar(numero1,numero2)
    print(soma)
except ValueError:
    print('voce digitou um numero invalido')
else:
    print('nada errado')




