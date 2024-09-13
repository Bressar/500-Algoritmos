# Algoritmo 38
# Cáculo de volume - lata de óleo

from math import pi

def calcular_volume_lata():
    while True:
        try:
            altura = float(input('Digite a altura da lata: '))
            raio = float(input('Digite o raio da lata: '))
            break
        except ValueError:
            print('Valor inválido, digite novamente!')

    #volume = 3.14159 * (raio ** 2) * altura
    volume = pi * (raio ** 2) * altura # é mais preciso, pi do módulo math tem 6 casas decimais

    print(f'O volume da lata é de: {volume}')
   
    
calcular_volume_lata()
