"""
Valor padrão para parâmetros
Valores padronizados podem ser enviados como parâmetro de uma função
Caso nenhum valor seja enviado, o valor padrão será utilizado
"""

def soma(x, y, z=0):
    if z:
        print(x + y + z)
    else:
        print(x + y)

soma(10, 2) # como nenhum outro valor foi passado como parâmetro, o valor padrão foi utilizado.
soma(10, 2, 20) # neste caso um valor foi passado, portanto o valor padrão foi substituido.

# Os valores padronizados também podem ser utilizados para definir parâmetros que podem ou não serem enviados.