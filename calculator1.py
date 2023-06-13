"""
projeto pratico de freecodecamp
calculadora em python
"""
num1=float(input('insira um numero:'))
num2=float(input('insira um numero:'))
op=str(input('insira a operação desejada:'))
soma=num1+num2
sub=num1-num2
m=num1*num2
div=num1/num2


#função que realiza as operações
def operations(num1,num2):
    if op=='+':
        print(f'a soma: {soma}')
        return soma
    elif op=='-':
        print(f'a subtração:{sub}')
        return sub
    elif op=='x':
        print(f'a multiplicação:{m}')
        return m
    elif op=='/' :
        print(f'a divisão:{div}')
        return div 
    else:
        print('operação inválida!')
        
 
      
            
        
#chamando a função      
operations(num1,num2)
