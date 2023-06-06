a=int(input('insira um numero'))
b=int(input('insira outro numero'))
def somar():
    return a + b 

#chamando a funçao
print(somar())
def dizeroi():
    print('oi')
dizeroi()
#com parametros
def cumprimento(nome):
   print(f'oi {nome}')

cumprimento('jeyjey')
def m(n1,n2):
    n1=int(input('numero'))
    n2=int(input('numero'))
    return n1 *n2


print(m(2,2))
def mult(n3,n4):
    print('hi')
    return n3 * n4
    

num1=int(input('numero'))
num2=int(input('numero'))

print(mult(num1,num2))

def novoUsuarioBanco(name,age):
    print(f'Bem vindo ao banco digital, {name}, {age} anos')
    return name,age

print(novoUsuarioBanco('jeyjey','20'))

