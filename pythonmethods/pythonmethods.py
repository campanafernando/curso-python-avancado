"""
useful methods on python:
len - quantas chaves
keys - iterável com chaves
values - iterável com valores
items - iterável com chaves e valores
setdefault - adiciona valor se a chave não existe
copy - retorna uma cópia rasa (shallow copy)
get - obtém uma chave
pop - apaga um item com a chave específicada
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""

pessoa = {
    'nome': 'Fernando',
    'idade': '22'
}

print(len(pessoa))
print(list(pessoa.keys())) # keys retorna as chaves do dicionário, e realizamos uma coerção com o método list para melhor visualização
print(list(pessoa.values())) # values retorna apenas o conteúdo das chaves
print(list(pessoa.items())) # items retorna chave e conteúdo do dicionário

print('=============================')

for chave, valor in pessoa.items(): # lembrar da possibilidade de acessar dois itens em um for
    print(chave, valor)

pessoa.setdefault('altura', '2 metros') # o método setdefault, seta um valor padrão para determinado item no dicionário, que poderá retornar ou não
print(pessoa['altura'])
print(pessoa)

print('==============================')

d1 = {
    "c1": 1,
    "c2": 2
}

d2 = d1

d2['c1'] = 1000 # como não foi feita nenhuma tratativa no dicionário, ao alterar a "cópia" alteramos o original.
print(d1)
print(d2)

print('==============================')

d3 = {
    "c3": 3,
    "c4": 4
}

d4 = d3.copy()  # como utilizamos o método copy, a lista que recebeu atribuição não afetou a original.

d4['c3'] = 3000  # lembrando que, o método copy só funciona com objetos imutáveis, objetos mutáveis (listas, por ex)
# isto acontece pq o copy é um "shallow copy", copia rasa, não acessa subníveis de um iterável
# ou seja o copy altera os dois valores mutáveis de uma lista/ dicionario, podendo gerar problemas em caso de mal uso

print(d4)
print(d3)

# como solução para este problema temos o módulo deepcopy (from copy import deepcopy)
print('==============================')

d5 = {
    'nome': 'Chico',
    'idade': '23'
}

print(d5.get('nome', None)) # o método get recolhe o valor de uma chave, também pode receber parâmetros default em caso de falta
print(d5['nome'])

# o método update atualiza o valor de um dicionario, o update também pode criar novas chaves

d5.update({
    'nome': 'Marcao', # o update também pode receber um iterável(listas ou tuplas, por ex)
    'chinelo': 'Havaianas'
})

print(d5) # a lista foi atualizada neste ponto