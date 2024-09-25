# Algoritmo 50
# Rendimento de poupança programada

def rendimento_poupanca_programada():
    while True:
        try:
            valor_aplicacao_mensal = float(input("Digite o Valor da Aplicação: € "))
            break
        except ValueError:
            print("ERRO! Valor inválido!")
    while True:
    # Convertendo a taxa de percentual para decimal (ex: 5% = 0.05)
        try:
            taxa = float(input("Digite o Valor da Taxa (ex: 5 para 5%): ")) / 100
            break
        except ValueError:
            print("ERRO! Valor inválido!")       
    while True:
        try:
            numero_meses = int(input("Digite o Número de Meses: "))
            break
        except ValueError:
            print("ERRO! Valor inválido!")

    if taxa == 0:
        valor_acumulado = valor_aplicacao_mensal * numero_meses
    else:
        valor_acumulado = valor_aplicacao_mensal * ((((1 + taxa)** numero_meses) - 1) / taxa )    
        
    print(f'Valor acumulado: € {valor_acumulado:.2f}')
    
    
rendimento_poupanca_programada()
