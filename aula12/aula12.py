num1 = input('Digite um número:')
num2 = input('Digite outro número:')
soma = num1+num2

if num1.isdigit() and num2.isdigit():
    num1 = int(num1)
    num2 = int(num2)

    print(f'Sua soma é {num1 +num2}')
else:
    print('Digite um número inteiro válido')