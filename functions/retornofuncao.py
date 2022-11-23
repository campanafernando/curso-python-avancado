"""
Closure e funções aninhadas
"""

def criar_saudacao():
    def saudar(saudacao, nome):
        return f'{saudacao}, {nome}!' #criando uma função que retorna outra função
    return saudar # nossa função retorna esta outra função

goodmorning = criar_saudacao() #nossa função irá retornar com os parâmetros estabelecidos na função central
goodnight = criar_saudacao()  #podemos nomea-la da forma que nos for interessante

listona = ['fernando', 'mateus', 'paulo']

for nome in listona:
    print(goodmorning('Bom dia', nome))