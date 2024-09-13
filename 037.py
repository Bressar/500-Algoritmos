# Algoritmo 37
# Conversor de temperatura Farenheit/Celsius

def conversor_temperatura():
    print('\n' + 'CONVERSOR DE MEDIDAS DE TEMPERATURA'.center(60))

    while True:
        print('--' * 30)   
        escolha = input('''Para converter de Celsius para Farenheit - prima [F]
Para converter de Farenheit para Celsius - prima [C] 
Para sair prima qualquer outra tecla. ''').strip().upper()

        if escolha == 'C':
            try:
                valor_farenheit = float(input('Insira o valor da temperatura em Farenheit: '))
                valor_celsius = (valor_farenheit -32) / 1.8
                print('--' * 25)
                print(f'{valor_farenheit} farenheit equivale a - > {valor_celsius:.2f} graus Celsius.')
            except ValueError:
                print('Valor inválido, digite novamente')
        elif escolha == 'F':
            try:
                valor_celsius = float(input('Insira o valor da temperatura em graus Celsius: '))
                # valor_farenheit = (9 * valor_celsius + 160) / 5 # pode ser esta fórmula tb
                valor_farenheit = (valor_celsius * 9 / 5) + 32
                print('--' * 25)
                print(f'{valor_celsius} graus Celsius equivale a -> {valor_farenheit:.2f} Farenheit.')
            except ValueError:
                print('Valor inválido, digite novamente')
        else:
            print('--' * 25)
            print('Encerrando o programa...')
            break
            
        
conversor_temperatura()
