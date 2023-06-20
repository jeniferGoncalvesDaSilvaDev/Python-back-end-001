#dicionarios 
#variavel multipla que possui chave e valor 
#seus valores, podem ser mutaveis 
""" 
banco de dados de um e-commerce, cujo vende produtos direcionados, ex: maquiagem que combina com a cor de seus olhos e de seu cabelo
"""
dict = {
    'name': 'jeyjey', 
    'age':26,
    'nacionalidade':'brasileira', 
    'corFavorita':'azul',
    'olhos':'verde', 
    'altura':1.55,
    'cabelo':'castanho', 
    'profissao':'dev full stack', 
    'fumante': False,
    'amigos':[ 'marlon', 'groot', 'duda', 'alan', 'polly', 'amanda', 'mika' , 'jo']
}
print(dict)
#imprimir só o nome 
print('usuario: ' + dict['name'] )
print(dict['age'])
for item in dict:
   if dict['profissao'] == 'dev full stack':
       print('bem vinda a nossa loja Dev!')
       break 

for i in dict['amigos']:
    if i == 'jo':
        print(i)
        break 



def verificarIdade():
        if dict['age']>=18:
            print('maior de idade')
            return dict['age']
        else:
            print('menor de idade')
            return dict['age']
        
        
print(verificarIdade())


def nacionalidade():
    for interaction in dict:
        if dict['nacionalidade'] == 'brasileira':
            print('voce fala português')
            break 
    return dict['nacionalidade']
            
            
print(nacionalidade())
