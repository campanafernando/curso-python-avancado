def format_cpf(self):
    fatia_um = self.cpf[:3]
    fatia_dois = self.cpf[3:6]
    fatia_tres = self.cpf[6:9]
    fatia_quatro = self.cpf[9:]
    return (
        "{}.{}.{}-{}".format(
            fatia_um,
            fatia_dois,
            fatia_tres,
            fatia_quatro
        )
    )