# listas e tuplas

lista = [
    #0            1            2
    ['Fernando', 'Campana', 'Felipe'], # 0
    ['João', 'Augusto', 'Marcos'], # 1
    ['Maria', 'Aline', 'Alice'] # 2
]

enumerada = enumerate(lista)
print(enumerada)
print(list(enumerada))
print(lista[2][2])