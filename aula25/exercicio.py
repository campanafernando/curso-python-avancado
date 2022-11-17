idade = int(input('Digite aqui a sua idade:\n'))

demaior = (idade >= 18)
msg = 'Pode acessar.' if demaior else 'Não pode acessar.'

print(msg)