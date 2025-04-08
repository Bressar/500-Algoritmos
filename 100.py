# Algoritmo 100
# Review de POO -> sei que não é nenhum algoritmo, mas vou deixar na lista assim mesmo :)


# exemplo 1
class Bike:
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro
        self.marcha = 1
    
        
    def buzinar(self):
        print("Bi! Bi!")
       
        
    def parar(self):
        print("Parando bicicleta...")
        print("Bicicleta parada.")
        
        
    def correr(self):
        print("Vummmmm...")
            
        
    def __str__(self):
        return f"{self.__class__.__name__}: {', ' .join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"    #Imprime o nome da classe e todoso os itens contatenados com o join
        
    """ def __str__(self): # versão Manual do __str__
        return f"Bicileta: cor={self.cor}, modelo={self.modelo}, ano={self.ano}, valor={self.valor}" """
        
    """ def get_cor(self):
        return self.cor """
        
        
    def trocar_marcha(self, nro_marcha):
        print("Trocando marcha") 
             
        def _trocar_marcha():
            if nro_marcha > self.marcha:
                print("Marcha trocada...")
            else:
                print("Não foi possível trocar a marcha")
        

    
b1 = Bike("red", "caloi", 2025, 500)  
b1.buzinar()
b1.parar()
b1.correr() 

print(f'Cor: {b1.cor}\nModelo: {b1.modelo}\nAno: {b1.ano}\nValor: {b1.valor}')


b2 = Bike("verde", "Monareta", 1977, 130)
b2.buzinar() # Bike.buzinar(b2)
#print(b2.get_cor())
print(b2) # imprime o metodo __str__  se ele não existisse mostraria apenas a localização do objeto na memória


