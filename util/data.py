class Data:
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        if self.dia < 10:
            data_str = f'0{self.dia}'
        else:
            data_str = str(self.dia)
        if self.mes < 10:
            data_str += f'/0{self.mes}'
        else:
            data_str += f'/{self.mes}'
        data_str += f'/{str(self.ano)}'

        return data_str