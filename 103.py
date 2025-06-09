# Algoritmo 103

# Entrar com um nome, idade e sexo de 2 pessoas. Imprimir o nome se a pessoa for
# do sexo masculino e tiver mais de 21 anos.

def filtro_idade_sex():
    
    for i in range(1,  4):
        while True:
            try:
                nome = str(input("Digite nome: ")).upper().strip()
                break
            except ValueError:
                print("Valor inválido! Tente de novo...")
        while True:       
                sexo = str(input("Digite o sexo [F] ou [M]: ")).upper().strip()
                if sexo == "F" or sexo == "M":
                    break
                else:
                    print("Valor inválido! Tente de novo...")
        while True:
            try:                    
                idade = int(input("Digite a idade: "))
                break
            except ValueError:
                print("Valor inválido! Tente de novo...")

        if idade > 21 and sexo == "F":
            print(f"Nome: {nome}")
            
            
