texto = 'Python'
novotexto = ''

for letra in texto:
    novotexto += f'{letra}{letra}'
print(novotexto)

for i in range(10, 0, -1):
    print(i, end=' ')