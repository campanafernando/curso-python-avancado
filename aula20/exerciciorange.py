# for numero in range(10):
#     print(numero+1)
#
# for numero2 in range(10, 0, -1):
#     print(numero2)

# for n in range(100):
#     if n % 2 == 0:
#         print(n)

nome = "Fernando"
novastring = ''

for letra in nome:
    if letra == "n":
        novastring = novastring + letra.upper()
    else:
        novastring += letra
print(novastring)