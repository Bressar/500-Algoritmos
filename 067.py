# Algoritmo 67
# Desconto de INSS

# Com a seguinte tabela de descontos
# <= 1200  - isento
# > 1200 e <= 2400 - 20%
# > 2400 e <= 4000 - 25%
# > 4000 - 30%

def calculo_INSS():
    while True:
        while True:
            try:
                salario = float(input("Digite o valor do sálario: R$ "))
                if salario > 0:
                    break
                else:
                    print("Erro! digite um valor positivo!")
            except ValueError:
                print("ERRO! digite um valor válido!")
                
        if salario <= 1200:
            print("--" * 20)
            print(f"Valor isento de tributação\nTotal a receber: R${salario:.2f}")
            print("--" * 20)
        elif salario > 1200 and salario <= 2400:
            desconto = salario * 0.2
            total = salario - desconto
            print("--" * 20)
            print(f"20% de tributação\nTotal a receber: R${total:.2f}")
            print("--" * 20) 
        elif salario > 2400 and salario <= 4000:
            desconto = salario * 0.25
            total = salario - desconto
            print("--" * 20)
            print(f"25% de tributação\nTotal a receber: R${total:.2f}")
            print("--" * 20) 
        else:
            desconto = salario * 0.3
            total = salario - desconto
            print("--" * 20)
            print(f"30% de tributação\nTotal a receber: R${total:.2f}")
            print("--" * 20) 
            
        print('--' * 20)
        sair = input("Pressione qualquer tecla para continuar, ou [S] para sair\n").strip().upper()
        if sair == "S":
            print('--' * 20)
            print("Encerrando o programa...")
            print('--' * 20)
            break    
  
        
calculo_INSS()
