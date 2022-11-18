print('LISTA DE COMPRAS')
lista_compras = []

while True:
    option = input('Selecione uma opção: \n [i]nserir, [a]pagar, [l]istar, [s]air: \n')
    if option == 'i':
        item = input('Selecione um item:')
        lista_compras.append(item)
        print(lista_compras)
        continue
    elif option == 'a':
        delete = int(input('Selecione um índice para apagar:'))
        if delete > len(lista_compras):
            print('Índice inválido. Número superior ao de itens da lista.')
        else:
            lista_compras.pop(delete)
        continue
    elif option == 'l':
        lista_enumerada = enumerate(lista_compras)
        print(list(lista_enumerada))
    elif option == 's':
        print('Até logo!')
        break
    else:
        print('Opção inválida.')

