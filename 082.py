# Algoritmo 082
""" Ler o percurso (km), tipo de carro, retornar o consumo estimado de combustível.
sabendo que carro:
    A -> faz 12 km por litro
    B -> faz  9 km por litro
    c -> faz  8 km por litro """
    
# Farei esse usando POO
    
class Carro:
    def __init__(self, consumo=1):
        self.consumo = consumo
 
        
carro_A = Carro(12)  
carro_B = Carro(9)    
carro_C = Carro(8)   


def calcular_consumo(distancia_km, consumo):
   consumo_litro = distancia_km / consumo
   return consumo_litro

try:
    percurso = int(input('Digite o percurso em KM: '))
    if percurso <= 0:
        raise ValueError("O percurso deve ser maior que zero.")
except ValueError as e:
    print(f"Entrada inválida: {e}")
    exit()
   
carro_escolhido= input('Digite o tipo de carro( A / B / C ): ').upper().strip()

if carro_escolhido == 'A':
    carro = carro_A
elif carro_escolhido == 'B':
    carro = carro_B
elif carro_escolhido == 'C':
    carro = carro_C
else:
    print("Erro! faça uma escolha válida!")
    exit()

print(f'Consumo estimado em litros: {calcular_consumo(percurso, carro.consumo)} ')    

    
# versão simples:
    