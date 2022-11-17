usuario = input('Nome do usuário:')
senha = input('Senha do usuário:')

usuario_bd = 'fernando'
senha_bd = '123'

if usuario not in usuario_bd:
    print('Usuário invalido')
elif senha not in senha_bd:
    print('Senha inválida')
if usuario_bd == usuario and senha_bd == senha:
    print('Logado com sucesso')