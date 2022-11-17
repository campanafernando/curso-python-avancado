string = 'O Brasil é pentacampeão mundial, o Brasil é foda'

lista = string.split(' ')  # a função split divide a string baseada no parâmetro selecionado, espaços, vírgulas, etc.

palavra = ''
contagem = 0
for valor in lista:
    qtdvezes = lista.count(valor)

    if qtdvezes > contagem:
        contagem = qtdvezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi {palavra}, aparecendo {contagem}x ')