# Algoritmo 74
# Se o nome começar com as letras A,D,M e S o cliente entra na promoção de descontos
# Salvar os clientes e pagamentos em um dicionário e apresentar o total de pagamentos.

clientes_e_valores ={}

while True:
    while True:
        try:
            print('--' * 30) 
            nome = str(input("Digite o nome: ")).strip().title()   
            if not nome: # Verifica se o nome está vazio após o strip
                raise ValueError("O nome não pode ser vazio ou conter apenas espaços.")
            if not all(part.isalpha() for part in nome.split()):
                raise ValueError("O nome deve conter apenas letras.")   
            break       
        except ValueError as e:
            print(f"Erro! {e}\n- Tente novamente!")
       
    while True:
        try:            
            valor_conta = float(input("Digite o valor da conta: "))
            if valor_conta > 0:
                break
            else:
                print("Valor da conta não pode ser inferior a € 1.00")
        except ValueError as e:
            print(f"Erro! {e} - Valor inválido!")

    if nome[0] in "ADMS":
        valor_desconto = round(valor_conta * 0.7, 2)
        clientes_e_valores[nome] = valor_desconto
        print('--' * 30) 
        print(f'{nome}! O valor da sua conta com desconto é de: €{valor_desconto}')
        print('--' * 30) 
    else:
        clientes_e_valores[nome] = valor_conta
        print('--' * 30) 
        print(f"Que pena {nome}!\nNesta semana o desconto não é para o seu bico!\nVai esperando que um dia sua vez chegará...")
        print('--' * 30) 
        
    continuar = input('[C] Continuar - [S] Sair ').strip().upper()
    if continuar == 'S':
        print('--' * 30) 
        print('Encerrando o programa...')
        print('--' * 30) 
        break

# Calculando o total dos pagamentos em 1 linha
total_recebido = round(sum(float(valor) for valor in clientes_e_valores.values()), 2)
 
# Calculando o total dos pagamentos usando uma lista
# valores_recebidos = []
# for valor in clientes_e_valores.values():
#     valores_recebidos.append(float(valor))
# total_recebido = round(sum(valores_recebidos) , 2)

# Exibindo os resultados
print('--' * 30) 
print("Resumo dos pagamentos:")
for nome, valor in clientes_e_valores.items():
    print(f'{nome} -> € {valor}')
print('**' * 30) 
print(f'TOTAL recebido: € {total_recebido}')
print('**' * 30) 
