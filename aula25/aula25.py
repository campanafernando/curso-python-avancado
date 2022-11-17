"""""
Operadores ternários em Python
"""""

logged_user = False

if logged_user:
    print('Logado')
else:
    print('Deslogado')
# maneira convencional

# operadores ternários
user_logged = False
msg = 'Usuário logado' if user_logged else 'Usuário precisa logar'
print(msg)