salas = [
    ['Wingslompsom', 'Wingsthompsom', 'Wingsmacacson'],
    ['Mordekelnon', 'Tommy Filfon', 'Fifulinon'],
    ['Titiuson', 'Nelsons', 'Nilsons', (0, 2, 4, 6, 8)]
]


lista = ['Maria', 'Helena', 'Eduarda', 1, 2, 3]

print(*lista)
print(lista)
print('******************')

for nome in lista:
    print(*lista)

# colocando um asterisco antes permite o desempacotamento
print('******************')
print(*lista, sep='\n')