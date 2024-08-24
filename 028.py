# Algoritmo 028
# Caixa de Eletrônico - Multibanco

print('=' * 40)
print('{:^40}'.format("Banco do Pobre"))
print('=' * 40)
valor = int(input('Que valor você quer sacar? R$'))
total = valor
céd = 50
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f"Total de {totcéd} cédulas de R${céd}")
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 40)
print("Volte sempre ao Banco do Pobre! Tenha um bom dia!")

'''
# Versão do Bressar
print("=" * 40)
print("{:^40}".format(" CHAVAS BANK "))
print("=" * 40)
valor_int = 0
resto = 0
while True:
    valor = int(input("Que valor você quer sacar? R$"))
    while valor >= 50:
        valor_int = valor // 50
        resto = valor % 50
        print(f"Total de {valor_int} cédulas de R$50")
        valor = resto
    while valor >= 20:
        valor_int = valor // 20
        resto = valor % 20
        print(f"Total de {valor_int} cédulas de R$20")
        valor = resto
    while valor >= 10:
        valor_int = valor // 10
        resto = valor % 10
        print(f"Total de {valor_int} cédulas de R$10")
        valor = resto
    while valor >= 1:
        valor_int = valor// 1
        valor = resto
        print(f"Total de {valor_int} cédulas de R$1")
        break
    sair = "SsCc"
    sair = str(input("Quer sair ou continuar? [S/C] ")).strip().upper()[0]
    print("----" * 10)
    while sair not in "SsCc":
        sair = str(input("Quer sair ou continuar? [S/C] ")).strip().upper()[0]
    print("----" * 10)
    if sair in "Ss":
        break
print("=====" * 10)
print("Volte sempre ao CHAVAS BANK! Tenha um bom dia!")

'''