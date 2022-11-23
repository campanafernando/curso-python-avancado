"""
O algoritmo de validação do CPF calcula o primeiro dígito verificador a partir dos 9 primeiros dígitos do CPF, 
e em seguida, calcula o segundo dígito verificador a partir dos 9 (nove) primeiros dígitos do CPF, 
mais o primeiro dígito, obtido na primeira parte.

O primeiro passo é calcular o primeiro dígito verificador, e para isso, separamos os primeiros 9 dígitos do CPF
(111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do 
número 2, como no exemplo abaixo:

10 9  8  7  6  5  4  3  2
1  4  3  8  7  0  6  0  6
10 36 24 56 42 0  24 0  12

Multiplicamos cada digito do CPF pelo respectivo número e somamos cada um dos resultados:
10+36+24+56+42+0+24+0+12 = 204

Pegamos o resultado obtido 204 e dividimos por 11.  Consideramos como quociente apenas o valor inteiro.

204 / 11  =    14  com resto 8

"""

print('ALGORITMO PARA VERIFICAÇÃO DE CPF:\n')
cpf = input('Digite aqui um CPF:\n').replace('.', '').replace('-', '')
while len(cpf) < 11:
    cpf = input('CPF inválido, tente novamente:\n').replace('.', '').replace('-', '')

nove_digitos = cpf[:9]
contador_regressivo = 10
resultado = 0

for digito in nove_digitos:
    resultado += int(digito) * contador_regressivo
    contador_regressivo -= 1

digito = resultado * 10 % 11
digito = digito if digito <= 9 else 0

nove_digitos2 = nove_digitos + str(digito)
contador_regressivo2 = 11
resultado2 = 0

for digito2 in nove_digitos2:
    resultado2 += int(digito2) * contador_regressivo
    contador_regressivo2 -= 1

digito2 = resultado2 * 10 % 11
digito2 = digito2 if digito2 <= 9 else 0

novocpf = f'{nove_digitos}{digito}{digito2}'
if novocpf == cpf:
    print('CPF VÁLIDO.')
else:
    print('CPF INVÁLIDO.')