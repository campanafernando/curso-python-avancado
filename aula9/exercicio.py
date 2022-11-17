nome = input('Qual seu nome?')
idade = int(input('Qual a sua idade?'))

idademenor = 18
idademaior = 60

if idade >= idademenor and idade <= idademaior:
    print(f'{nome} pode pegar o empréstimo')
else:
    print(f'{nome} não pode pegar o empréstimo')