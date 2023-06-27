#´para abrir arquivos externos, usa-se a funçao open("nome do arquivo e sua extensao")
#e ler usa-se a função read()
#para passar os parametros externos r e w, dentro do open, eh para ler e/ou editar arquivos
#para fechar arquivos-usa-se o metodo close. A variavel.close()
#o metodo readable(), retorna um valor boolenao, para verificar se eh legivel
#o metodo readlines(), retorna uma lista dos itens de cada linha
#o metodo readline, le um, o item[0] do arquivo
file1= open('countries.txt','r')
print(file1.readable())
print(file1.read())
#loop
#le cada linha do arquivo, tanto faz com readlines e readline
for line in file1.readline():
    print(line)
file1.close()