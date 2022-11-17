senha = '123456'
senhadigitada = ''
contador = 0

while senhadigitada != senha:
    senhadigitada = input(f'Senha digitada, tentativa nº{contador}:')

    contador += 1
print(f'{contador} tentativas.')
