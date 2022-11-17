print('CALCULADORA PYTHON')
n1 = input('Digite o primeiro número: \n')
n2 = input('Digite o segundo número: \n')
operadores = input('Selecione um operador: (+-*/)\n')
while True:
    try:
        n1float = float(n1)
        n2float = float(n2)
        nvalidos = True
    except:
        nvalidos = None

    if nvalidos is None:
        print('Um ou mais números digitados são inválidos.')
        continue

    operadorespermitidos = "+-*/"
    if operadores not in operadorespermitidos:
        print('Um ou mais operadores são inválidos.')
        continue

    if len(operadores) > 1:
        print('Digite apenas um operador aritmético.')
        continue

    print('Realizando sua conta. Confira o resultado abaixo:\n')

    if operadores == '+':
        print(f'O resultado da soma é: {n1float + n2float}')
    elif operadores == '-':
        print(f'O resultado da subtração é: {round(n1float - n2float), 2}')
    elif operadores == '*':
        print(f'O resultado da multiplicação é: {round (n1float * n2float), 2}')
    elif operadores == '/':
        print(f'O resultado da divisão é {round(n1float / n2float), 2}')

    sair = input('Quer sair? [s]im:')
    sair = sair.lower()
    sair = sair.startswith('s')
    if sair is True:
        break