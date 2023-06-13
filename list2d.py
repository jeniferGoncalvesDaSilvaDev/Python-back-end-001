#lista 2d, eh uma lista dentro de muma lista
my_list=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#acessar o primeiro item da primeira lista
print('primeira lista-primeiro item')
print(my_list[0][0])
#acessar o primeiro item da segunda lista
print('segunda lista-primeiro item')
print(my_list[1][0])
#acessar o primeiro item da terceira lista
print('terceira lista-primeiro item')
print(my_list[2][0])
#for dentro de for para acesso dinamico-nested loop
#imprime x quantidade de vezes, sendo x o numero de listas em uma lista
#for listas in my_list:
    #print(my_list)

#acessar a primeira lista apenas
for lista in my_list:
    for linha in lista:
        print('primeiro item da lista')
        print(linha)