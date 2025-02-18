# Algoritmo 085
""" 
Algoritmo que: fornece o valor do lucro de uma venda de acordo com uma tabela"""

tabela_lucro = [
    [10, 70],  # index 0 = valor e index 1 = lucro em %
    [30, 50],
    [50, 40],
    [float('inf'), 30]  # Inf para cobrir qualquer valor acima de 50
]

nome_produto = input('Digite o nome do produto:\n').strip().title()
valor_compra = float(input('Digite o valor da compra:\n'))

for limite, lucro in tabela_lucro:
    if valor_compra <= limite:
        valor_venda = valor_compra + (valor_compra * lucro) / 100
        break  # Sai do loop assim que encontrar a faixa correta

print(f'O produto: {nome_produto} será vendido por €{valor_venda:.2f}')


print('--' * 30)


# Versão 1
tabela_lucro = [
                [10, 70], # index 0 = valor e index 1 = lucro em %
                [30, 50],
                [50, 40],
                [50, 30]
                ]

valor_venda = float(0)

nome_produto = input('Digite o nome do produto:\n').strip().title()
valor_compra = float(input('Digite o valor da compra:\n'))

if valor_compra <= tabela_lucro[0][0]:
    valor_lucro = tabela_lucro[0][1]    
    valor_venda = valor_compra + (valor_compra * valor_lucro) / 100
    
elif valor_compra <= tabela_lucro[1][0]:
    valor_lucro = tabela_lucro[1][1]    
    valor_venda = valor_compra + (valor_compra * valor_lucro) / 100
    
elif valor_compra <= tabela_lucro[2][0]:
    valor_lucro = tabela_lucro[2][1]    
    valor_venda = valor_compra + (valor_compra * valor_lucro) / 100
    
else:
    valor_lucro = tabela_lucro[3][1] 
    valor_venda = valor_compra + (valor_compra * valor_lucro) / 100
    
  
print(f'O produto: {nome_produto} será vendido por €{valor_venda:.2f}')



