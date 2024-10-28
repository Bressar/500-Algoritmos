# Algoritmo 70
# Cálculo de Peso Ideal, salvando os dados em um dicionário

dicionario_consulentes = {}

print('--' * 30)
print("Para saber seu Peso Ideal. Digite:")

while True:
    nome = input("Nome: ").strip().title()

    while True:
        try:
            altura = float(input("Altura (em metros, ex.: 1.8): "))
            break
        except ValueError:
            print("Erro, Digite um número válido")
            print('--' * 30)
    while True:    
        sexo =  input("Sexo: [M] ou [H]\n").strip().upper()
        print('--' * 30)
        if sexo == "M":
            peso_ideal = (62.1 * altura) - 44.7
            dicionario_consulentes[nome] = round(peso_ideal, 2)
            print(f"Seu peso ideal é de {peso_ideal:.2f} Kg") 
            print('--' * 30) 
            break
        elif sexo == "H":
            peso_ideal = (72.7 * altura) - 58
            dicionario_consulentes[nome] = round(peso_ideal, 2)
            print(f"Seu peso ideal é de {peso_ideal:.2f} Kg")
            print('--' * 30) 
            break
        else:
            print("Valor inválido! Tente novamente...")
            print('--' * 30) 

    continuar = input("Quer continuar? [S] Sim ou [N] Não?\n").strip().upper()
    if continuar == "N":
        print("Encerrrando o programa...")
        print('--' * 30) 
        break
           
print("Resumo dos consulentes e seus pesos ideais:")
for nome, peso_ideal in dicionario_consulentes.items():
    print(f'{nome} -> Peso ideal: {peso_ideal:.2f} Kg')
print('--' * 30) 

print(dicionario_consulentes)# for debug
       