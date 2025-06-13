# Algoritmo 110
""" Implemente uma classe Veiculo que represente um carro com marca, modelo e ano. Crie um método que verifique se o carro é considerado antigo (mais de 20 anos). """

# TODO: Crie a Classe Veiculo e armazene sua marca, modelo e ano como atributos:

from datetime import datetime

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
    
#   TODO: Implemente o método verificar_antiguidade e calcule a diferença entre o ano atual e o ano do veículo:
    def verificar_antiguidade(self):
        ano_atual = datetime.now().year
        if ano_atual - self.ano > 20:
            return "Veículo Antigo"
        else:
            return "Veículo novo"
        

marca = input().strip()
modelo = input().strip()
ano = int(input().strip())

# Instanciando o objeto e verificando a antiguidade
veiculo = Veiculo(marca, modelo, ano)
print(veiculo.verificar_antiguidade())
