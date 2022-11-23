
def multiply(a, b):
    return a * b

var = multiply(20, 2)
print(var)

var2 = multiply(2, 10)
print(var2)

def multiplyall(*args):
    valor = 1
    for item in args:
        valor *= item
        print(valor, end=' ')


var3 = multiplyall(2, 2, 10, 2, 3, 2)


teste = 2*2*10*2*3*2
print(f'\n{teste}')


def imppar(a):
    if a %2 == 0:
        return 'par'
    return'impar'

print(imppar(2))
print(imppar(3))