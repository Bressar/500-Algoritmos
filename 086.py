# Algoritmo 86
# Cálculo de IMC a partir dos dados de uma tabela

def calculo_IMC():
    tabela_IMC = [
        [20, 'abaixo do peso'],
        [25, 'normal'],
        [30, 'excesso de peso'],
        [35, 'obesidade'],
        [float('inf'), 'obesidade mórbida'] #Inf para cobrir qualquer valor acima de 50
    ] # Em Python, float('inf') representa um número infinito.
      # (imc <= float('inf') sempre será True).
    
    while True:
        print("=-=-" * 7)
        print(">>>  CALCULADORA DE IMC <<<\n"
                "<<< Insira os seus dados >>>")
        print("=-=-" * 7)
        while True:
            try:
                peso = float(input('Informe o seu peso em kg:\n'))
                break
            except ValueError:
                print('Valor inválido, tente novamente')
        while True:    
            try:
                altura = float(input('Informe sua altura em metros:\n'))
                break
            except ValueError:
                print('Valor inválido, tente novamente')
                
        imc = peso / (altura ** 2)

        for imc_tabela, resultado in tabela_IMC:  
            if imc <= imc_tabela:
                mensagem = resultado
                break  # Sai do loop assim que encontrar a faixa correta
            
        print('--' * 25)
        print(f'Com a altura de: {altura} m\ne o peso de {peso} kg\nResultado: {mensagem}')
        print('--' * 25)
        
        sair = str(input("Para Sair[S] - para Continuar prima qualquer tecla. ")).strip().upper()[0] # [0]: pega o primeiro caractere da string que o usuário digitou.
        if sair == "S":
            print("--" * 30)
            print("Saindo do Programa...")
            print("--" * 30)
            break

calculo_IMC()
