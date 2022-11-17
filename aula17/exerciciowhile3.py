while True:
    print()
    num1 = input('Digite um número:')
    num2 = input('Digite outro número:')
    operador = input('Escolha um operador:')
    sair = input('Deseja sair? [s]im/[n]ão')
    if sair == 's':
        break

    if not num1.isnumeric() or not num2.isnumeric():
        print('Você precisa digitar um número!')
        continue

    if operador == '+':
        print(num1 + num2)
    elif operador == '-':
        print(num1 - num2)
    elif operador == '*':
        print(num1 * num2)
    elif operador == '/':
        print(num1 / num2)
    else:
        print('Operador inválido')

