numero_str = input('Digite um número para ser dobrado:')

try:
    print('STR:', numero_str)
    numero_float = float(numero_str)
    print('FLOAT:', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * numero_float}')
except:
    print('Isso não é um número.')

print(id(numero_str))