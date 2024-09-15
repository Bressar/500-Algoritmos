# Algoritmo 40
# Prestação em atraso

def calculo_prestacao_em_atraso():
    # Inicializando as variáveis de controle como False
    valor_prestacao_ok = False
    taxa_ok = False
    tempo_ok = False

    # Loop para receber o valor da prestação até ser válido
    while not valor_prestacao_ok:
        if not valor_prestacao_ok:
            try:
                valor_prestacao = float(input('Digite o valor da prestação: '))
                valor_prestacao_ok = True  # Se não houver erro, definido como True
            except ValueError:
                print('--' * 30)
                print('Erro! Digite um valor numérico para a prestação.')
                print('--' * 30)
    
    # Loop para receber o valor da taxa até ser válido
    while not taxa_ok:  
        if not taxa_ok:
            try:
                taxa = float(input('Digite o valor da taxa: '))
                taxa_ok = True  # Se não houver erro, definido como True
            except ValueError:
                print('--' * 30)
                print('Erro! Digite um valor numérico para a taxa.')
                print('--' * 30)
    
    # Loop para receber o tempo até ser válido
    while not tempo_ok:    
        if not tempo_ok:
            try:
                tempo = int(input('Digite o tempo (número de meses): '))
                tempo_ok = True  # Se não houver erro, definido como True
            except ValueError:
                print('--' * 30)
                print('Erro! Digite um valor numérico inteiro para o tempo.')
                print('--' * 30)

    # Cálculo da prestação em atraso
    valor_prestacao = valor_prestacao + (valor_prestacao * (taxa / 100) * tempo)
    print('--' * 30)
    print(f'Valor da prestação em atraso é: € {valor_prestacao:.2f}')
    print('--' * 30)


calculo_prestacao_em_atraso()

        
        
# versão + simples, se houver um erro repete todas as entradas...
# def calculo_prestacao_em_atraso():
#     while True:
#         try:
#             valor_prestacao = float(input('Digite o valor da prestação: '))
#             taxa = float(input('Digite o valor da taxa: '))
#             tempo = int(input('Digite o tempo (número de meses): '))
#             break
#         except ValueError:
#             print('Erro! digite novamente')
            
#     valor_prestacao = valor_prestacao + (valor_prestacao * (taxa/100) * tempo)

#     print(f'Valor da prestação em atraso é: € {valor_prestacao:.2f}')

# calculo_prestacao_em_atraso()
