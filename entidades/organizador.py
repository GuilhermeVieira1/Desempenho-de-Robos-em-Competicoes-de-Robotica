organizadores = []

def get_organizadores():
    return organizadores

def inserir_organizador(organizador):
    organizadores.append(organizador)

class Organizador:
    def __init__(self, nome, contato, pais, website, ano_fundacao):
        self.nome = nome
        self.contato = contato
        self.pais = pais
        self.website = website
        self.ano_fundacao = ano_fundacao

    def __str__(self):
        formato = '{:<13} {:<17} {:<15} {:<31} {:<4}'
        organizador_formatado = formato.format(self.nome, self.contato, self.pais, self.website, str(self.ano_fundacao))

        return organizador_formatado