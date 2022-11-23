import random
from random import randint

cpf = str(randint(000000000000, 99999999999))
print(cpf)

for _ in range(10):
    novedigitos = ''
    for i in range(11):
        novedigitos += str(random.randint(0, 9))

    print(novedigitos)