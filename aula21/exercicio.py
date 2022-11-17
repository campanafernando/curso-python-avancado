secretword = 'esquilo'
letrasdigitas = []
chances = 3

while True:
    if chances <= 0:
        print('Você perdeu!')
        break

    letra = input('Digite uma letra:')

    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue

    letrasdigitas.append(letra)

    if letra in secretword:
        print(f'A letra {letra} existe na palavra secreta, continue assim.')
    else:
        print(f'Ops, a letra {letra}, não existe na palavra secreta.')
        letrasdigitas.pop()

    secretotemporario = ''
    for letrasecreta in secretword:
        if letrasecreta in letrasdigitas:
            secretotemporario += letrasecreta
        else:
            secretotemporario = secretotemporario + '*'
    print(secretotemporario)
    if secretotemporario == secretword:
        print(f'Você descobriu a palavra secreta! Parabéns! Palavra secreta: {secretword}')
    else:
        print(f'A sua palavra está assim {secretotemporario}.')

    if letra not in secretword:
        chances -= 1

    print(f'Você ainda tem {chances} chances.')