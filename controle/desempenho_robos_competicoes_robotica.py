from util.data import Data
from util.gerais import imprimir_objetos
from entidades.robo import get_robos, inserir_robo, Robo
from entidades.organizador import get_organizadores, inserir_organizador, Organizador

def cadastrar_robos():
    inserir_robo(Robo('Megamentes', 'Seguidor De Linha', 25, 25, Data(9, 11, 2022), 'Eduardo Martins'))
    inserir_robo(Robo('Techvikings', 'Seguidor De Linha', 20, 20, Data(15, 3, 2023), 'Ana Silva'))
    inserir_robo(Robo('ThunderBots', 'Seguidor De Linha', 20, 25, Data(22, 7, 2023), 'Carlos Almeida'))
    inserir_robo(Robo('CetroEragon', 'Seguidor De Linha', 18, 18, Data(5, 1, 2024), 'Fernanda Oliveira'))
    inserir_robo(Robo('Titas', 'Seguidor De Linha', 25, 30, Data(11, 10, 2024), 'Guilherme Barnabé'))
    inserir_robo(Robo('ByteForce', 'Seguidor De Linha', 24.5, 25, Data(27, 9, 2022), 'Geovani Michels'))
    inserir_robo(Robo('RoboWarriors', 'RoboCup', 23, 22, Data(13, 2, 2023), 'Lucas Pereira'))
    inserir_robo(Robo('CyberGliders', 'RoboCup', 26, 27, Data(19, 5, 2023), 'Mariana Rocha'))
    inserir_robo(Robo('Robodroids', 'RoboCup', 26, 24, Data(1, 8, 2023), 'Rafael Souza'))
    inserir_robo(Robo('Machina', 'RoboCup', 21, 23, Data(28, 12, 2023), 'Beatriz Lima'))
    inserir_robo(Robo('DynamoBots', 'RoboCup', 24, 26, Data(3, 4, 2024), 'Renato Siqueira'))
    inserir_robo(Robo('CodeMasters', 'RoboCup', 25, 28, Data(15, 6, 2024), 'Aline Santos'))
    inserir_robo(Robo('PixelDance', 'Artistica', 20, 22, Data(14, 2, 2023), 'Lucas Carvalho'))
    inserir_robo(Robo('ArtBotics', 'Artistica', 21, 23, Data(18, 6, 2023), 'Camila Menezes'))
    inserir_robo(Robo('PaintTech', 'Artistica', 19.5, 21, Data(25, 9, 2023), 'Henrique Silva'))
    inserir_robo(Robo('MotionMinds', 'Artistica', 22, 24, Data(9, 12, 2023), 'Gabriela Azevedo'))
    inserir_robo(Robo('DanceBots', 'Artistica', 20.5, 23, Data(15, 3, 2024), 'Thiago Ferreira'))
    inserir_robo(Robo('Artitude', 'Artistica', 21, 22.5, Data(7, 7, 2024), 'Vanessa Castro'))
    inserir_robo(Robo('SumoRex', 'Sumo', 27, 30, Data(12, 1, 2023), 'João Freitas'))
    inserir_robo(Robo('TitanForce', 'Sumo', 28, 31, Data(5, 4, 2023), 'Priscila Barros'))
    inserir_robo(Robo('GladiatorBot', 'Sumo', 29, 32, Data(11, 7, 2023), 'Bruno Costa'))
    inserir_robo(Robo('IronClash', 'Sumo', 30, 33, Data(17, 10, 2023), 'Patrícia Andrade'))
    inserir_robo(Robo('HeavyWeight', 'Sumo', 29, 34, Data(4, 1, 2024), 'Carlos Silva'))
    inserir_robo(Robo('MegaSumo', 'Sumo', 28.5, 32.5, Data(10, 5, 2024), 'Marcela Moreira'))
    inserir_robo(Robo('WarriorZ', 'Combate', 32, 35, Data(8, 2, 2023), 'Fernando Dias'))
    inserir_robo(Robo('CrimsonFury', 'Combate', 31, 34, Data(14, 5, 2023), 'Sofia Borges'))
    inserir_robo(Robo('BladeRunner', 'Combate', 30.5, 36, Data(22, 8, 2023), 'Diego Faria'))
    inserir_robo(Robo('SteelRage', 'Combate', 33, 37, Data(3, 11, 2023), 'Larissa Ribeiro'))
    inserir_robo(Robo('PowerCrusher', 'Combate', 32, 35.5, Data(17, 2, 2024), 'Eduardo Cardoso'))
    inserir_robo(Robo('IronGiant', 'Combate', 31.5, 36.5, Data(29, 6, 2024), 'Juliana Costa'))

def cadastrar_organizadores():
    inserir_organizador(Organizador('UFMS','(67) 3345-7000','Brasil','https://www.ufms.br/',1962))
    inserir_organizador(Organizador('IEEE', '(800) 678-4333', 'Estados Unidos', 'https://www.ieee.org/',1884))
    inserir_organizador(Organizador('FIRST', '(603) 666-3906', 'Inglaterra','https://www.firstinspires.org/', 1989))
    inserir_organizador(Organizador('VEX Robotics', '(903) 453-0802', 'Estados Unidos', 'https://www.vex.com/',2005))
    inserir_organizador(Organizador('RoboCup', '+49 711 729 4712','Alemanha','https://www.robocup.org/', 1997))


if __name__ == "__main__":
    cadastrar_robos()
    cadastrar_organizadores()
    print('\nDesempenho de Robos em Competições de Robótica: ')
    imprimir_objetos(cabecalho='Robos Cadastrados\n Nome, Categoria, Altura, Largura, Data_Criacao, Desenvolvedor', objetos=get_robos())
    imprimir_objetos(cabecalho='Organizadores Cadastrados\n Nome, Contato, Pais, Website, Ano Criacao', objetos=get_organizadores())