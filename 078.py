# Algoritmo 078
# Análise de saldo médio para concessão de crédito - salvando dados em uma lista de tuplas

lista_cliente = [] # lista dos elegíveis a aa ter crédito

while True:
    
    cliente = [] # a cada loop cria uma lista nova
    
    while True:
        nome = input("Digite seu nome: ").strip().title()   
        cliente.append(nome)
        try:
            saldo_medio = float(input("Digite o saldo médio/anual: "))
            cliente.append(round(saldo_medio, 2))
            break
        except ValueError as e:
            print(f'ERRO! - {e}\nDigite um valor válido!')

    if saldo_medio < 501:
        credito = 0
    elif saldo_medio < 1001:
        credito = saldo_medio * 0.3
    elif saldo_medio < 3001:
        credito = saldo_medio * 0.4
    else:
        credito = saldo_medio * 0.5 

    print('--' * 30)
    if credito == 0:
        print(f'{nome}, você é muito pobre!\nNão tem direito a crédito nenhum! Passa ontem...') 
        cliente.append(credito)
        # pobre é considerado cliente, mas não  entra na lista de elegíveis para empréstimo.
    else:   
        print(f"{nome}, com um saldo médio de € {saldo_medio}\nO valor do crédito disponível é de: € {credito}")
        cliente.append(round(credito, 2))
        lista_cliente.append(tuple(cliente)) # se tiver $$ entra na lista dos elegiveis
    print('--' * 30)
    
    sair = input('[C] Continuar - [S] Sair\n').strip().upper()
    if sair == "S":
        print()
        break
    
print('--' * 30)   
for cliente in lista_cliente:
    print(f'Nome: {cliente[0]} - Saldo médio: €{cliente[1]} - Valor do crédito: €{cliente[2]}')
    print('--' * 30)
