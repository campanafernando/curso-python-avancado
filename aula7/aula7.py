nome = input('Digite seu nome:')
idade = int(input('Digite aqui sua idade'))
altura = float(input('Digite sua altura:'))
peso = int(input('Digite aqui seu peso:'))
ano = 2022 - idade
imc = round((peso/altura**2), 2)

print(f'Seu nome é {nome} e você nasceu no ano {ano}, e seu imc é {imc}')
