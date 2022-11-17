"""""
Split, Join e Enumerate em Python
"""""

string = "O Brasil é o país do futebol. O Brasil é foda."

string2 = string.split('/')
print(string2)
string3 = string.split(' ')
print(string3)

for valor in string3:
    print(f'A palavra {valor} apareceu {string3.count(valor)}x vezes.')

print(len(string3))

print(len('59.920.949/0001-52'))

print(len('82995283602'))

# (r"^\(?[1-9]{2}\)? ?(?:[2-8]|9[1-9])[0-9]{3}\-?[0-9]{4}$")