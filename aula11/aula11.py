usuario = input('Digite seu nome:')
qtdchar = len(usuario)

while qtdchar <= 6:
    usuario = input('Digite seu nome, com mais de 6 caracteres:')  #Len mais utilizada em strings
    print(f'Seu nome possui {len(usuario)-0} caracteres.')
    print('Cadastrado com sucesso')
