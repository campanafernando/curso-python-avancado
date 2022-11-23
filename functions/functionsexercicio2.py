def multi_tri_quadri():
    def multiplicar(numero):
        return numero * 2, numero * 3, numero * 4
    return multiplicar


numero = multi_tri_quadri()

print(numero(5))

def criar_multiplicador(multiplicador):
    def multiply(numero):
        return numero * multiplicador
    return multiply

var = criar_multiplicador(2)
print(var(2))