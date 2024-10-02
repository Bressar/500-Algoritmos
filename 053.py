# Algoritmo 53
# Ler um número, se for positivo imprimir seu inverso, caso contrário imprimiro valor absoluto. 

def inverso_absoluto():
    while True:
        try:
            numero = float(input("Digite um número: "))
            if numero == 0:
                print("O inverso de zero não existe.") 
            else:
                break
        except ValueError:
            print("Valor inválido! Digite novamente")  
                               
    if numero > 0:
        print("Valor Inverso: ", 1 / numero)
    else:
        print("Valor Inverso: ", numero * -1) 
        
inverso_absoluto()
