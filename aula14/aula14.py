num = input('Digite um número inteiro:')

if num.isdigit():
    num = int(num)
    if num %2 == 0:
        print('Seu número é par.')
    else:
        print('Você digitou um número ímpar.')
else:
    print('Digite um número inteiro!')