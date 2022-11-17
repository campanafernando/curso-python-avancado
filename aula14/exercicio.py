horario = input('Digite um horário entre 0 e 23 horas:')

if horario.isdigit():
    horario = int(horario)
    if horario < 0 or horario > 23:
        print('Horário deve estar entre 0 e 23!')
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 18:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Digite um horário entre 0 e 23!')