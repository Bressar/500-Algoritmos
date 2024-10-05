# Algoritmo 60
# Filtrando pessoas por idade e sexo

pessoas_aceitas = []
pessoas_recusadas = []

while True:
    print('--' * 20)  
    while True:
        try:
            nome = input("Nome: ").strip().title() # title() para capitalizar cada parte
            # Verifica se o nome contém apenas letras ou espaços
            if not all(part.isalpha() for part in nome.split()):
                raise ValueError("O nome deve conter apenas letras.")
            else:
                break
        except ValueError as e:
            print(f"ERRO! {e}")
            print('--' * 10)    
    while True: 
        sexo = str(input("Sexo [F] ou [M]: ")).upper().strip()[0]
        if sexo not in "FM":
            print('ERRO! Escolha "F" ou "M" ')
            print('--' * 10)
        else:
            break    
    while True:
        try:
            idade = int(input("Idade: "))
            if idade < 0 or idade > 110:
                print("Digite uma idade válida!")
                print('--' * 10)
            else:    
                break
        except ValueError:
            print("ERRO! Digite um número válido para a idade.")
            print('--' * 10)

    print('--' * 20)  
    
    if sexo != "F" or idade > 25:
        pessoas_recusadas.append(nome)
        print("RECUSADA!") 
        print('--' * 10)      
    else:
        print("ACEITA!")
        print('--' * 10)
        pessoas_aceitas.append(nome)
        
    sair = input("Para continuar pressione qualquer tecla.\nPara sair pressione [S]\n").upper().strip()
    if sair == "S":
        break  

print("\n","**" * 20, "\n")
   
print('--' * 10)
print("APROVADOS")
print('--' * 10)
for i in pessoas_aceitas:
    print(f"- {i}") 
    
print("\n","**" * 20, "\n")

print("REPROVADOS")
print('--' * 10)
for i in pessoas_recusadas:
    print(f"- {i}")
print('--' * 10)    
    