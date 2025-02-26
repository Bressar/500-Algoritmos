# Algoritmo 93

# Sistema Bancário (simples )

menu = """
------------
=== MENU ===
[d] Depósito
[s] Sacar
[e] Extrato
[q] Sair
------------
"""

saldo= 0
numero_saques = 0
limite_saque = 3
limite_valor = 1500
saque_diario =[]
# extrato = {{'saques' : []},
#            {'depositos': []}}
extrato = [[],
           []]

def linha():
    print('--' * 10)

while True:
    
    opcao = input(menu).strip().lower()
    
    if opcao == "d":
        while True:
            try:
                valor_deposito = float(input('Depositar: € '))
                if valor_deposito > 0:
                    saldo += valor_deposito 
                    extrato[0].append(valor_deposito )
                    print(f'Depósito no valor de: € {valor_deposito:.2f}')
                    linha()
                    break
                else:
                    print('Erro! Valor inválido!')
            except ValueError:
                print('Valor inválido! Digite novamente') 
        
 
    elif opcao == 's':
        while True:
            try:
                valor_saque = float(input('Sacar: € '))
                if numero_saques + 1 > limite_saque: # numero_saques só é incrementado após todas as verificações
                    print('Limite de 3 saques diários excedido!')
                    break
                elif saldo < valor_saque:
                    print('Saldo insuficiente! Operação cancelada!')
                elif valor_saque > 500:
                    print('Valor máximo de €500 por saque excedido!')
                    break
                elif sum(saque_diario) > limite_valor:
                    print('Valor máximo €1500 diários excedido!')
                    break
                else:
                    numero_saques += 1
                    saldo -= valor_saque
                    saque_diario.append(valor_saque)
                    extrato[1].append(valor_saque)
                    print(f'Saque no valor de: € {valor_saque:.2f}')
                    linha()
                    break  
                      
            except ValueError:
                print('Valor inválido! Digite novamente') 
                                
    elif opcao == 'e':
        print('=====  EXTRATO  =====')
        contador1 = 0
        for item in extrato[0]:
            contador1  += 1
            linha()
            print(f'Depósito {contador1}: +€ {item}')
        linha()
        contador2= 0
        for item in extrato[1]:
            contador2 += 1
            linha()
            print(f'Saque {contador2}: -€ {item}')
        linha()     
        print(f'Saldo atual: € {saldo:.2f}')
        linha() 
        
    elif opcao == 'q':
        linha()
        print('Encerrando o programa...')
        linha()
        break
    
    else:
        print('Operação inválida, selecione novamente a opção desejada!')
        
        
