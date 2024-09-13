# Algoritmo 039
# Consumo de combustível - viagem de carro

""" Calcular a quantidade de litros de combustível gastos em uma viagem, de um carro que faz 12km com um litro.
Fornecer tempo gasto na viagem e velocidade média

fórmulas - > distancia = tempo * Velocidade
         - > litros usados = distância // 12
         
         Apresentar valores de:
         - velocidade média
         - tempo gasto
         - distância percorrida
         - quantidade de litros gastos
        """

def consumo_combustivel():
    while True:
        try:        
            tempo = float(input('Digite o tempo gasto: '))
            velocidade_media = float(input('Digite a velocidade média: '))
            break
        except ValueError:
            print('Valor inválido, digite novamente.')

    distancia = tempo * velocidade_media
    litros = distancia / 12

    print('--' * 20)
    print(f'- Velocidade média: {velocidade_media} km/hora\n'
    f'- Tempo gasto: {tempo} horas\n'
    f'- Distância percorrida: {distancia} Km\n'
    f'- Quantidade de litros gastos: {litros:.2f} litros')
    print('--' * 20)
  
    
consumo_combustivel()
