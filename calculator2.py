"""
melhorando o código anterior, usando loops
"""
print('Caro(a) usuário(a)! Ao inserir as operações, usa: \n. + para adição\n. - para subtração\n. x para muliplicação\n . / para divisão\n')
def operations():
    while True:
        n1= float(input('insira um numero: '))
        n2=float(input('insira um numero:'))
        op=str(input('insira a operação desejada:'))
        ux= str(input('deseja continuar?Insira s para sim e n para não :)'))
        if ux =='n':
            print('obrigado(a)!')
            break 
        elif ux =='S':
            print('comando inválido!')
        elif ux=='N':
            print('comando inválido!')
        
        elif op=='+':
            print(f'a soma: {n1+n2}')
        elif op=='-':
            print(f'a subtração: {n1-n2}')
        elif op=='x':
            print(f'a multiplicação: {n1*n2}')
        elif op=='/':
            print(f'a divisão: {n1/n2}')
        else:
            print('operação inválida! Tente novamente :)')
            
            
        
        
        
        
        
operations()
    