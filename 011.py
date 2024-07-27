# Algoritmo 011
# Entrar com um número inteiro de 3 casas e imprimir o algarismo da casa das dezenas.

while True:
    try:
        numero = int(input('Digite um número inteiro com 3 casas decimais: '))
        if numero < 100 or numero > 999:
            print('Erro! o número não tem 3 casas decimais')
        else:
            numero_resultado = (numero // 10) % 10
            #numero_resultado = (numero % 100) // 10
            
            #numero_resultado = (numero / 10) % 10 
            # -> dará um resultado com duas casa decimais: ex: se numero = 135, resultado = 3.5
            
            print(f'A casa das dezenas de {numero} é: [{numero_resultado}]')
            break
    except:
        print('Valor inválido, tente novamente')


# Quando montar uma expressão usando / e % ,
# se % vier antes colocar entre () para priorizar a operação!
