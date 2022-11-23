"""
high order functions
"""


def saudacao(msg, nome):
    return f'{msg}, {nome}!'


def executa(funcao, *args):
    return funcao(*args)


executar = executa(saudacao, 'Bom dia', 'Fernandex') # executando uma função dentro de outra funcção

print(executar)