# Algoritmo 45
# Cálculo de IMC

def calculo_imc():
    print("=-=-" * 7)
    print(">>>  CALCULADORA DE IMC <<<\n"
          "<<< Insira os seus dados >>>")
    print("=-=-" * 7)
    while True:
        while True:
            try:
                peso = float(input('Insira o seu peso: '))
                break
            except ValueError:
                print('Valor inválido! Digite novamente.') 
        while True:        
            try:      
                altura = float(input('Insira a sua altura (em metros): '))
                break
            except ValueError:
                print('Valor inválido! Digite novamente.')
                
        imc = peso / (altura ** 2)
        
        print(f"Seu IMC é de {imc:.2f}: ", end ="")
        if imc < 18.5:
            print(">> BAIXO PESO.")
        elif imc < 25:
            print(">> NORMAL.")
        elif imc < 30:
            print(">> SOBREPESO.")
        elif imc <= 40:
            print(">> OBESIDADE.")
        else:
            print(">> OBESIDADE MÓRBIDA.")
        
        print("--" * 30)    
      
        sair = str(input("Para Sair[S] - para Continuar prima qualquer tecla. ")).strip().upper()[0] # [0]: pega o primeiro caractere da string que o usuário digitou.
        if sair == "S":
            print("--" * 30)
            print("Saindo do Programa...")
            print("--" * 30)
            break

calculo_imc()
