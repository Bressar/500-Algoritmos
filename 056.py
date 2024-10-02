# Algoritmo 56
# Calculadora

def calculadora():
    while True:
        while True:
                print("\n***************")
                print("* CALCULADORA *")
                print("***************")
                print("""[ + ] Somar
[ - ] Subtrair
[ * ] Multiplicar
[ / ] Dividir
[ S ] Sair
                    """)
                opcao = input("Digite uma opção: ").strip().upper()
                if opcao in"+-*/S":
                    break
                else:
                    print("--" * 15)
                    print("Opção não disponível!")
                    print("--" * 15)
                    
        def valores():
            num1 = float(input("Digite o 1° número: "))
            num2 = float(input("Digite o 2° número: "))
            return num1, num2

        if opcao == "+":
            num1, num2 = valores()
            resultado = num1 + num2
            print(f'Soma -> {num1} + {num2} = {resultado}')       
        elif opcao == "-":
            num1, num2 = valores()
            resultado = num1 - num2
            print(f'Subtração -> {num1} - {num2} = {resultado}')         
        elif opcao == "*":
            num1, num2 = valores()
            resultado = num1 * num2
            print(f'Multiplicação -> {num1} * {num2} = {resultado}')        
        elif opcao == "/":
            num1, num2 = valores()
            resultado = num1 / num2
            print(f'Divisão -> {num1} / {num2} = {resultado}')       
        elif opcao == "S":
            print("--" * 15)
            print("Encerrando...")
            print("--" * 15)
            break       


calculadora()
