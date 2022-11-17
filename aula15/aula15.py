"""""
Formatando valores com modificadores:

:s - Texto (strings)
:d - Inteiros (int)
:f - Número de ponto flutuante (float)

:.(NÚMERO)f - Quantidade de casas decimais
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

"""""

num = 13
num2 = 7
div = num/num2
print(f'{div:.2f}')

num3 = 1
print(f'{num3:0>10}')

num4 = 243
print(f'{num4:0^10}')

num5 = 748
print(f'{num5:0<10}')

nome = 'Fernando Campana'

print(nome.lower())
print(nome.upper())