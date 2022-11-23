"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e escopo local.
O escopo global é o escopo onde todo o código é alcançavel.
O escopo local é o escopo onde apenas os nomes do mesmo local podem ser alcançados.
"""

z = 1 # está no escopo global

def escopo3():
    z = 10 # dentro da função, que possui seu próprio escopo z recebe outro valor

    def outrafuncao(): # a função aninhada recebe outro valor, e pode acessar o valor do escopo anterior, mas não o global.
        w = 20
        print(z, w)

    outrafuncao() # aqui z irá executar z como o valor de 10
    print(z + 1)

print(z) # valor de z global
escopo3() # valor de z printado pela função, esta função também executa a outra função
print(z)