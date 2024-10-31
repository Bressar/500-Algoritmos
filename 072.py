# Algoritmo 72
# Ler um número e retornar o mês correspondente, esse é simplezinho :)
# Ler a idade e informar a classe eleitoral, usando dicionários para reduzir o código.

# Algoritmo A
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



# Algoritmo B - nesse caso fazer um dicionário é besteira :(
""" classe_eleitoral ={
    'abaixo_16': 'Não-eleitor',
    'entre_18_65': 'Eleitor obrigatório',
    'entre_16_18_maior_65': 'Eleitor facultativo'
}

idade = int(input("Digite sua idade: "))

if idade < 16:
    print(f'{classe_eleitoral["abaixo_16"]}')
elif idade < 18 or idade > 65:
    print(f'{classe_eleitoral["entre_16_18_maior_65"]}')
elif idade >=18 and idade < 65:
    print(f'{classe_eleitoral["entre_18_65"]}')
 """

# melhor o tradicional
try:
    idade = int(input("Digite sua idade: "))
except ValueError:
    print('ERRO! digite um número')

if idade < 16:
    print('Não-eleitor')
elif idade < 18 or idade > 65:
    print('Eleitor facultativo')
elif idade >= 18 and idade <= 65:
    print('Eleitor obrigatório')
