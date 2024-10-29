# Algoritmo 71
# Receber uma idade e cadastrar a partir de uma determinada categoria, registar em um lista de dicionários

# infantil_A  =  5 a 7
# infantil_B  = 8 a 10
# juvenil_A   = 11 a 13
# juvenil_B  =  14 a 17 anos
# senior    =  maiores de 18

# Dicionários de categorias
infantil_a = {}
infantil_b = {}
juvenil_a = {}
juvenil_b = {}
senior = {}

while True:
    # entradas nome e idade + validações
    while True:
        try:
            print('--' * 30)
            nome = input("Nome: ").strip().title()
            if not all(part.isalpha() for part in nome.split()):
                raise ValueError("O nome deve conter apenas letras.")
            else:
                break
        except ValueError:
            print("Valor inválido! tente novamente!")    
    while True:
        try:
            idade =  int(input("Idade: "))
            break
        except ValueError:
            print("ERRO! Valor inválido!")
    
    # verificação de categoria        
    if idade < 5:
        print("Erro! a idade deve ser superior a 4 anos")
    elif  idade >= 5 and idade <= 7:
        infantil_a[nome] = 'Infantil A'
    elif  idade >= 8 and idade <= 10:
        infantil_b[nome] = 'Infantil B'      
    elif idade >= 11 and idade <= 13:
        juvenil_a[nome] = 'Juvenil A'
    elif idade >= 14 and idade <= 17:
        juvenil_b[nome] = 'Juvenil B'
    else:
        senior[nome] = 'Senior'        
    continuar = input("Quer continuar? [S] Sim ou [N] Não?\n").strip().upper()
    if continuar == "N":
        print("Encerrrando o programa...")
        print('--' * 30) 
        break

# Lista com todas as categorias   
categorias = [infantil_a, infantil_b, juvenil_a, juvenil_b, senior,]   


# Outputs  
for dicionario in categorias:
    for nome, categoria in dicionario.items():
        print(f'{nome} -> Categoria: {categoria}')
  
for item in categorias:
    print(item, end="\n")# for debug

