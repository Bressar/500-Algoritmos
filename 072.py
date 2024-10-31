# Algoritmo 72
# Ler um número entre 1 e 12 e retornar o mês correspondente, esse é simplezinho :)

meses = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}

while True:
    try:
        escolha = int(input("Digite um número entre 1 e 12 para saber o mês correspondente. "))
        if escolha < 1 or escolha > 12:
            print("Erro! Escolha entre 1 e 12!")
        else:
            break
    except ValueError:
        print("Erro! Escolha entre 1 e 12!")
        
print(f"O {escolha}° mês é {meses[escolha]}.")
# como fazer tudo em 1 linha usando um dicionário ao invés de ifs, elses e match cases

