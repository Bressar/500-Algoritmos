# Algoritmo 108 
# Carrinho de compras que permita adicionar produtos e calcular o valor total da compra

""" Descrição
Entrada
Lista de produtos adicionados ao carrinho (cada um com nome e preço).
Saída
Lista dos produtos adicionados e o total da compra. """

# Lista para armazenar os produtos e preços
carrinho = []
total = 0.0

# Entrada do número de itens
n = int(input().strip())

# Loop para adicionar itens ao carrinho
for _ in range(n):
    linha = input().strip()
    # Encontra a última ocorrência de espaço para separar nome e preço
    posicao_espaco = linha.rfind(" ")
    # Separa o nome do produto e o preço
    item = linha[:posicao_espaco]
    preco = float(linha[posicao_espaco + 1:])
    carrinho.append((item, preco)) # Adiciona ao carrinho
    total += preco
    
   # Impressão dos itens e cálculo do total
for item, preco in carrinho:
    print(f"{item}: R${preco:.2f}")
print(f'Total: R${total:.2f}')


