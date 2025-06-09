# Algoritmo 105
# Cálculo de descontos usando um dicionário

print("Iniciando o programa...")

preco_str = input("Digite o preço: ")
print(f"Preço digitado: {preco_str}")

preco = float(preco_str)

cupom = input("Digite o cupom: ").strip().upper()
print(f"Cupom digitado: {cupom}")

descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

if cupom in descontos:
    desconto = descontos[cupom]
    saida = preco - (desconto * preco)
    print(f"Preço final: {saida:.2f}")
else:
    print("Cupom inválido.")




""" # DEBUG de uma código fantasma que não roda ...

print("Iniciando o programa...")

preco_str = input("Digite o preço: ")
print(f"Preço digitado: {preco_str}")

preco = float(preco_str)

cupom = input("Digite o cupom: ").strip().upper()
print(f"Cupom digitado: {cupom}")



descontos = {
    "DESCONTO10": 0.10,
    "DESCONTO20": 0.20,
    "SEM_DESCONTO": 0.00
}

preco = float(input().strip())
cupom = input().strip().upper()

if cupom in descontos:
    desconto = descontos[cupom]
    saida = preco - (desconto * preco)
    print(f"{saida:.2f}") 
else:
    print("Cupom inválido.")
 """