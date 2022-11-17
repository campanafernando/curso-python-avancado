

frase = 'o rato roeu a roupa do rei de roma'
print(frase)
tamanho_frase = len(frase)
contador = 0
novastring = ''

userinput = input('Qual letra deseja colocar maiúscula?\n')

while contador < tamanho_frase:
    letra = frase[contador]
    if letra == userinput:
        novastring += userinput.upper()
    else:
        novastring += letra
    contador += 1

print(novastring)