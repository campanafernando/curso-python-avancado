"""
Argumentos nomeados e não nomeados em Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

def soma(x, y, z):
    #definição
    print(f'{x=} {y=} {z=} | x+y+z = {x+y+z}')

soma(10, 20, 12) # não nomeado
soma(y=12, z=22, x=2) # nomeado
#argumentos posicionais dependem da posição, e você pode invertê-las definindo a posição na chamada.

#misturar argumentos não nomeados com nomeados NÃO é uma boa prática.