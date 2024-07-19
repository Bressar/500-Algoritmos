## Algoritmo 004
# Fim de semana

def fim_de_semana(previsao='sol'):
    if previsao != 'sol':
        print('Almoçar\nVer TV\nDormir')
    else:
        print('Vou à praia')
        
fim_de_semana('chuva')
print('ou')
fim_de_semana()