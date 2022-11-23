"""
retornando vários parametros numa mesma função
"""

def soma(*args):
    total = 0
    for item in args:
        total += item
        print(total)


soma(21, 22, 23, 24)

print('================')

somatotal = soma(10, 100, 1000, 10000, 100000)

print('================')

print(sum([10, 20, 30, 40])) # a função sum soma valores iteráveis, como listas e tuplas.