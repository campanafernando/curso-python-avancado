"""""
For/Else
Python
"""""

variavel = ['Maria', 'aJoão', 'Otávio']


for item in variavel:
    if item.lower().startswith('j'):  # dentro do laço nós alteramos o valor Booleano da variável para verdadeiro
        break
else:
    print('Não existe uma palavra que começa com J.')