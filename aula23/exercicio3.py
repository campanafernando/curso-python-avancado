# função enumerate

string = 'O Brasil é penta'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(f'O indice é {indice} e o valor é {valor}')
# a função enumerate enumera indices de uma lista, através de tuplas.

