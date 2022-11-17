import re
cpf = '99999999999'
cpfPontuado = re.sub(r'(\d{3})(\d{3})(\d{3})(\d{2})', r'\1.\2.\3-\4', cpf)
print(cpfPontuado)

cnpj = '99999999999999'
cnpjPontuado = re.sub(r'(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})', r'\1.\2.\3/\4-\5', cnpj)
print(cnpjPontuado)

telefone = '552132118663'
padrao = "([0-9]{2}|[0-9]{2})?([0-9]{2})([0-9]{4,5})([0-9]{4})"

resposta = re.search(padrao, telefone)
print('+{}{}{}{}'.format(resposta.group(1),  resposta.group(2), resposta.group(3), resposta.group(4)))
