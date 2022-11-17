"""""
Listas em Python
fatiamendo
append, insert, pop, del, clear, extend, + 
min, max
range
"""""

texto = "VaIndicelor"
lista = ["V", "AINDICE", "L", "O", "R"]

# é importante compreender a diferença entre indice, e posição.
print(texto[1], lista[1])
# no primeiro print, texto irá nos trazer a posição[1] = letra A.
# no segundo print, lista[1] irá nos trazer o item completo determinado pelo índice.

lista2 = ["A", "B", "C", "D", 22.5]
lista2[4] = 13.4  # neste exemplo, alteramos o valor de um item da lista através de seu índice.

print(lista2)

print(lista2[0:4])  # "fatiando" a lista para que nos exiba somente os primeiros 4 itens.
print(lista2[::4])  # neste caso, estamos printando o primeiro valor e "pulando" direto para o útlimo item. "::"


lista3 = [1, 2, 3]
lista4 = [4, 5, 6]

lista5 = lista3 + lista4  # somando o valor de duas listas
print(lista5)

lista6 = [8, 9, 10]
lista7 = [11, 12, 13]

lista6.extend(lista7)  # atribuindo o valor de uma lista a outra com a função extend
# a função extend também pode ser utilizada para adicionar outros valores.

lista7.extend('a')

print(lista6)
print(lista7)

lista8 = [14, 15, 16]
lista8.append('b')  # a função append é utilizada para adicionar valores a listas, sempre adicionando a última posição.
print(lista8)

lista9 = [17, 18, 19]
lista9.insert(0, 'novo item')  # a função insert adiciona um novo item a lista, desta vez podendo selecionar a posição.
print(lista9[0])

lista10 = [20, 21, 22, 23, 24, 25]
del(lista10[0:3]) # desta forma, a função del irá deletar do índice 0 ao 3(20, 21, 22), também podemos excluir apenas 1.
print(lista10)

#criando listas com python

lista11 = list(range(0, 40, 8))
# aqui utilizamos a função list para criação da lista, e a função range para determinar que queremos de 0 a 40 apenas os múltiplos de 8


print(lista11)
for i in lista11:
    print(i)

lista12 = ['String', True, 1, 1.5]

for element in lista12:
    print(f'O tipo de element é {type(element)} e seu valor é {element}')