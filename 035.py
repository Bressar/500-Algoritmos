# Algoritmo 035
# Consumo de energia / Kw
# 
# Em 2024 -> SM R$ 1.412,00.

""" Sabendo que 100 quilowats custa um sétimo do salário mínimo.
    receba o valor do salário mínimo e a quantidade de Kw gastos na residência, calcular e imprimir:
    - O valor em R$ de cada kilowatt
    - o valor a ser pago
    - o novo valor a ser pago por essa residência com 10% de desconto """

def conta_de_luz():
    while True:
        try:   
            salario_minimo = float(input('Entre com o salário mínimo: '))
            quantidade_KW = float(input('Entre com a quantidade em quilowatt: '))
            break
        except ValueError:
            print('Erro! digite um número válido')
            
    #preco = salario_minimo / 7 # preço de 100 kw
    preco_kw = salario_minimo / 700 # ou preco / 100 
    valor_pagamento = preco_kw * quantidade_KW
    valor_desconto = valor_pagamento * 0.9 # desconto de 10%
    
    print('--' * 20)
    print(f'Salário mínimo: R${salario_minimo:.2f}')
    print(f'Preço de 1 quilowatt: R${preco_kw:.2f}')  # precisão para 6 casas decimais
    print(f'Valor total sem desconto: R${valor_pagamento:.2f}')
    print(f'Valor com desconto: R${valor_desconto:.2f}')
    print('--' * 20)

conta_de_luz()
