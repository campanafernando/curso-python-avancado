pessoa = {}

chave = 'nome'
sobrenome = 'sobrenome'

pessoa[chave] = 'Paulao'
pessoa[sobrenome] = 'Cardoso'
lista = []

if pessoa.get('sobrenome') is None:
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])
