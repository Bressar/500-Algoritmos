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
limite = 1500
numero_saques = 0
limite_saque = 3

saque_diario =[]

while True:
    
    opcao = input(menu).strip().lower()
    
    if opcao == "d":
        while True:
            try:
                valor_deposito = float(input('Depositar: € '))
                if valor_deposito > 0:
                    saldo += valor_deposito  
                    print(f'Depósito no valor de: € {valor_deposito:.2f}')
                    print('---' * 20)
                    break
                else:
                    print('Erro! Valor inválido!')
            except ValueError:
                print('Valor inválido! Digite novamente') 
        
        
    elif opcao == 's':
        while True:
            try:
                valor_saque = float(input('Sacar: € '))
                if  numero_saques < limite_saque and saldo > valor_saque and valor_saque <= 500 and sum(saque_diario) < limite:
                    numero_saques += 1
                    saldo -= valor_saque
                    saque_diario.append(valor_saque)
                    print(f'Saque no valor de: € {valor_saque:.2f}')
                    print('---' * 20)
                    break
                else:
                    if numero_saques > limite_saque:
                        print('Limite de 3 saques diários excedido!')
                        break
                    elif saldo < valor_saque:
                        print('Saldo insuficiente! Operação cancelada!')
                        break
                    elif valor_saque > 500:
                        print('Valor máximo de €500 por saque excedido!')
                        break
                    elif sum(saque_diario) > limite:
                        print('Valor máximo €1500 diários excedido!')
                        break
                    else:
                        print('Erro! Valor inválido!')            
            except ValueError:
                print('Valor inválido! Digite novamente') 

        
    elif opcao == 'e':
        print('=== EXTRATO ===')
        print(f'Saldo atual: € {saldo:.2f}')
        
    elif opcao == 'q':
        print('Encerrando o programa...')
        break
    
    else:
        print('Operação inválida, selecione novamente a opção desejada!')
        
        
    