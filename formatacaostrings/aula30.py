nome = input('Digite seu nome:')

print(f'Seu nome é {nome}')
print(f'A primeira letra do seu nome é {nome[:1]}')
print(f'Seu nome de trás pra frente é {nome[::-1]}')
if ' ' in nome:
    print('Seu nome contém espaços.')
else:
    print('Seu nome não contém espaços.')
print(f'Seu nome tem {len(nome)} letras')
print(f'A última letra do seu nome é {nome[-1:]}')