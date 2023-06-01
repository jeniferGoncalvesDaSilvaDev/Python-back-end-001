paises= ['Inglaterra', 'Japão','Estados Unidos','Alemanha','Coreia do Sul','China']
#primeira posiçao
#print(paises[0])
#ultima posiçao- o indice -1, representa o utomo item da lista
#print(paises[-1])
for p in paises:
    if p=='Japão':
        print('alfabeto: hiragana, katakana, kanji')
        break
print('alfabeto verificado')
#metodos de listas
#se usar * co um numero, retorna o mesmo numero inserido na lista-retorna os itens da lista varias vezes
lista1=[1,2,3,4,5]
lista3=[5,7,99,102,56]
a = lista1[0] + lista3[0]
print(a)

lista2=['morango','maça','banana','pessego','goiaba']
#juntar as listas
#o metodo extend, junta 2 listas
#o metodo insert, insere um item de acordo com a posiçao da lista
#lista1.extend(lista2)
#print(lista1)
#print(lista2)
#print(f'a lista {lista2}, tem {len(lista2)} items')
lista2.insert(1,'kiwi')
lista2.insert(2,'manga')
lista2.insert(3,'melancia')
lista2.insert(4,'melao')
lista2.append('uva')


for f in lista2:
    if len(lista2)<=10:
        print(f'a lista foi atualizada: {lista2} e tem {len(lista2)} items')
        break
if len(lista2)>10:
    print('nao eh possivel adicionar mais frutas!')    


print(len(lista2))
#para obter o indice de um item da lista
for fruta in lista2:
    print(lista2.index(fruta))
    print(fruta)
    
    
print('finish')
#count, retorna o numero de vezes que tal item, aparece na lista
print(lista2.count('morango'))