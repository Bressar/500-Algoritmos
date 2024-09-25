# Algoritmo 46
# Taxa de juros / rendimento

def calculo_taxa_de_juros():
    while True:
        try:
            deposito = float(input("Valor do depósito: "))
            break
        except ValueError:
            print('ERRO! Valor inválido')
            print('--'*20)
    while True:
        try:
            taxa = float(input("Valor da Taxa: "))
            break
        except ValueError:
            print('ERRO! Valor inválido')
            print('--'*20)
        
    valor = (deposito*taxa) / 100
    total = deposito+valor 

    print('--'*20)
    print(f'Valor do depósito: € {deposito:.2f}\n'
        f'Valor da taxa: {taxa:.2f} %\n'
        f'Valor dos rendimentos: € {valor:.2f}\n'
        f'TOTAL: € {total:.2f}')
    print('--'*20)
    
calculo_taxa_de_juros()
