robos = []

def get_robos():
    return robos

def inserir_robo(robo):
    robos.append(robo)

class Robo:
    def __init__(self, nome, categoria, altura, largura, data_criacao, desenvolvedor):
        self.nome = nome
        self.categoria = categoria if categoria in ('Seguidor De Linha', 'RoboCup', 'Artistica', 'Sumo', 'Combate') else 'Indefinido'
        self.altura = altura
        self.largura = largura
        self.data_criacao = data_criacao
        self.desenvolvedor = desenvolvedor

    def __str__(self):
        formato = '{:<13} {:<18} {:<7} {:<7} {:<11} {:<17}'
        robo_formatado = formato.format(self.nome, self.categoria, f'{self.altura:.1f}cm', f'{self.largura:.1f}cm', str(self.data_criacao), self.desenvolvedor)

        return robo_formatado