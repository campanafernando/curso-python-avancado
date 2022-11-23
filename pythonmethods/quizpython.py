print('QUIZ PERGUNTAS E RESPOSTAS PYTHON:')

perguntas =[
    {
    'Pergunta': 'Quanto é 2+2?',
    'Opções': '1, 2, 3, 4',
    'Resposta': '4'
    },
    {
    'Pergunta': 'Quanto é 10*10?',
    'Opções': '10, 100, 1, 1000',
    'Resposta': '100'
    },
    {
    'Pergunta': 'Quanto é 25 + 225?',
    'Opções': '2225, 250, 255, 275',
    'Resposta': '250'
    }
]
acertos = []

while True:
    print('Seja bem vindo ao quiz.\n')
    print('Primeira pergunta:', perguntas[0]['Pergunta'])
    print('Opções:', perguntas[0]['Opções'])
    resposta = input('Digite sua resposta:')
    if resposta == perguntas[0]['Resposta']:
        print('Parabéns! Acertastes\n')
        acertos.append(resposta)
    else:
        print('Errooouu...\n')
    pass
    print('Segunda pergunta:', perguntas[1]['Pergunta'])
    print('Opções:', perguntas[1]['Opções'])
    resposta_2 = input('Digite sua resposta:')
    if resposta_2 == perguntas[1]['Resposta']:
        print('Parabéns! Acertou!\n')
        acertos.append(resposta_2)
    else:
        print('ERROOUUU..\n')
    pass
    print('Terceira pergunta:', perguntas[2]['Pergunta'])
    print('Opções:', perguntas[2]['Opções'])
    resposta_3 = input('Digite sua resposta:')
    if resposta_3 == perguntas[2]['Resposta']:
        acertos.append(resposta_3)
        print('Parabéns! Acertou!\n')
    else:
        print('Errouuuuu...\n')
    pass
    print(f'{len(acertos)} acerto(s) de 3!')
    print('Jogo finalizado até mais!')
    acertos.clear()
    break