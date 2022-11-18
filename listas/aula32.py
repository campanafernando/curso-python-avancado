"""""
Listas em Python
Tipo list: Mutável
Conhecimentos reutilizáveis: índices e fatiamento
Métodos úteis: append, insert, pop, del, clear, extend+
"""""

lista = [123, True, 'fofo', 1.2, []]

print(lista)
print(bool(lista))
print(len(lista))

for i in lista:
    if i == lista[2]:
        print(i)